import sys
import os
import pandas as pd
from datetime import datetime

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database.database import engine, init_db, get_session
from src.database.models import Base, Crop, MarketData

def create_tables():
    """Create all database tables."""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

def load_initial_crops():
    """Load initial crop data."""
    print("Loading initial crop data...")
    
    crops = [
        {
            'name': 'Rice',
            'water_requirement': 1500,
            'carbon_footprint': 2.7,
            'soil_suitability': 'clay,loamy',
            'growth_period_days': 120
        },
        {
            'name': 'Wheat',
            'water_requirement': 450,
            'carbon_footprint': 1.8,
            'soil_suitability': 'loamy,sandy',
            'growth_period_days': 120
        },
        {
            'name': 'Corn',
            'water_requirement': 500,
            'carbon_footprint': 2.0,
            'soil_suitability': 'loamy,silt',
            'growth_period_days': 90
        },
        {
            'name': 'Soybeans',
            'water_requirement': 450,
            'carbon_footprint': 1.5,
            'soil_suitability': 'loamy,clay',
            'growth_period_days': 100
        }
    ]
    
    session = get_session()
    try:
        for crop_data in crops:
            crop = Crop(**crop_data)
            session.add(crop)
        session.commit()
        print("Initial crop data loaded successfully!")
    except Exception as e:
        print(f"Error loading crop data: {e}")
        session.rollback()
    finally:
        session.close()

def load_market_data():
    """Load initial market data from CSV."""
    print("Loading market data...")
    
    try:
        market_data = pd.read_csv('data/market_researcher_dataset.csv')
        
        session = get_session()
        try:
            for _, row in market_data.iterrows():
                market_entry = MarketData(
                    crop_id=row['crop_id'],
                    region=row['region'],
                    price_per_kg=row['price'],
                    demand_level=row['demand_level'],
                    date_recorded=datetime.now()
                )
                session.add(market_entry)
            session.commit()
            print("Market data loaded successfully!")
        except Exception as e:
            print(f"Error loading market data: {e}")
            session.rollback()
        finally:
            session.close()
            
    except FileNotFoundError:
        print("Warning: Market data file not found. Skipping market data import.")

def main():
    """Main function to set up the database."""
    print("Starting database setup...")
    
    # Create tables
    create_tables()
    
    # Load initial data
    load_initial_crops()
    load_market_data()
    
    print("Database setup completed!")

if __name__ == "__main__":
    main() 