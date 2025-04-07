from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import pandas as pd

from ..database.database import get_db
from ..database.models import Farmer, Crop, Recommendation, MarketData
from ..agents.farmer_advisor import FarmerAdvisor, FarmerProfile
from ..agents.market_researcher import MarketResearcher

router = APIRouter()

# Load data (this would be replaced with actual data loading)
try:
    farmer_data = pd.read_csv('data/farmer_advisor_dataset.csv')
    market_data = pd.read_csv('data/market_researcher_dataset.csv')
except FileNotFoundError:
    print("Warning: Dataset files not found. Using mock data.")
    farmer_data = pd.DataFrame()
    market_data = pd.DataFrame()

# Initialize agents
farmer_advisor = FarmerAdvisor(farmer_data)
market_researcher = MarketResearcher(market_data)

@router.post("/farmers/", response_model=dict)
async def create_farmer(
    farmer: FarmerProfile,
    db: Session = Depends(get_db)
):
    """Create a new farmer profile."""
    db_farmer = Farmer(
        name=farmer.name,
        location=farmer.location,
        farm_size=farmer.farm_size,
        soil_type=farmer.soil_type,
        water_availability=farmer.water_availability
    )
    db.add(db_farmer)
    db.commit()
    db.refresh(db_farmer)
    return {"farmer_id": db_farmer.farmer_id, "message": "Farmer profile created successfully"}

@router.get("/recommendations/{farmer_id}")
async def get_recommendations(
    farmer_id: int,
    db: Session = Depends(get_db)
):
    """Get farming recommendations for a specific farmer."""
    farmer = db.query(Farmer).filter(Farmer.farmer_id == farmer_id).first()
    if not farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")
    
    # Create farmer profile
    farmer_profile = FarmerProfile(
        name=farmer.name,
        location=farmer.location,
        farm_size=farmer.farm_size,
        soil_type=farmer.soil_type,
        water_availability=farmer.water_availability,
        preferred_crops=None,
        budget=10000  # This would come from the farmer's actual data
    )
    
    # Get recommendations from both agents
    crop_recommendations = farmer_advisor.get_crop_recommendations(farmer_profile)
    
    # Get market analysis for recommended crops
    crops = [rec['crop'] for rec in crop_recommendations]
    market_analysis = market_researcher.generate_market_report(
        crops,
        farmer_profile.location,
        farmer_profile.farm_size
    )
    
    # Combine recommendations
    final_recommendations = []
    for crop_rec, market_rec in zip(crop_recommendations, market_analysis):
        combined_rec = {
            **crop_rec,
            'market_analysis': market_rec,
            'overall_score': (
                crop_rec['sustainability_score'] * 0.4 +
                market_rec['recommendation_score'] * 0.6
            )
        }
        final_recommendations.append(combined_rec)
    
    # Sort by overall score
    final_recommendations.sort(key=lambda x: x['overall_score'], reverse=True)
    
    # Store recommendations in database
    for rec in final_recommendations[:3]:  # Store top 3 recommendations
        db_recommendation = Recommendation(
            farmer_id=farmer_id,
            crop_id=1,  # This would be the actual crop ID
            sustainability_score=rec['sustainability_score'],
            profitability_score=rec['market_analysis']['recommendation_score'],
            water_efficiency_score=rec['sustainability_metrics'].water_efficiency,
            details=str(rec)  # Convert to string for storage
        )
        db.add(db_recommendation)
    
    db.commit()
    
    return {
        "farmer_id": farmer_id,
        "recommendations": final_recommendations,
        "timestamp": datetime.utcnow().isoformat()
    }

@router.get("/market-analysis/{region}")
async def get_market_analysis(
    region: str,
    crops: Optional[List[str]] = None,
    db: Session = Depends(get_db)
):
    """Get market analysis for specific crops in a region."""
    if not crops:
        crops = ['rice', 'wheat', 'corn', 'soybeans']  # Default crops
    
    market_report = market_researcher.generate_market_report(
        crops=crops,
        region=region,
        farm_size=10.0  # Default farm size for analysis
    )
    
    return {
        "region": region,
        "market_analysis": market_report,
        "timestamp": datetime.utcnow().isoformat()
    }

@router.get("/sustainable-practices/{farmer_id}/{crop}")
async def get_sustainable_practices(
    farmer_id: int,
    crop: str,
    db: Session = Depends(get_db)
):
    """Get sustainable farming practices for a specific crop."""
    farmer = db.query(Farmer).filter(Farmer.farmer_id == farmer_id).first()
    if not farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")
    
    farmer_profile = FarmerProfile(
        name=farmer.name,
        location=farmer.location,
        farm_size=farmer.farm_size,
        soil_type=farmer.soil_type,
        water_availability=farmer.water_availability,
        preferred_crops=[crop],
        budget=10000  # This would come from the farmer's actual data
    )
    
    practices = farmer_advisor.generate_sustainable_practices(
        farmer_profile,
        crop
    )
    
    return {
        "farmer_id": farmer_id,
        "crop": crop,
        "sustainable_practices": practices,
        "timestamp": datetime.utcnow().isoformat()
    } 