import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from pydantic import BaseModel

class MarketTrend(BaseModel):
    crop: str
    current_price: float
    predicted_price: float
    demand_level: str
    price_trend: str
    confidence_score: float

class MarketResearcher:
    def __init__(self, market_data: pd.DataFrame):
        """Initialize the Market Researcher agent with historical market data."""
        self.market_data = market_data
        self.demand_levels = ['Low', 'Medium', 'High']
        self.price_trends = ['Decreasing', 'Stable', 'Increasing']
        
    def analyze_price_trends(self, crop: str, region: str) -> Dict:
        """Analyze historical price trends for a specific crop in a region."""
        # This would use actual historical price data
        mock_prices = {
            'rice': {'mean': 400, 'std': 50},
            'wheat': {'mean': 300, 'std': 30},
            'corn': {'mean': 250, 'std': 25},
            'soybeans': {'mean': 500, 'std': 60}
        }
        
        crop_stats = mock_prices.get(crop.lower(), {'mean': 300, 'std': 30})
        current_price = np.random.normal(crop_stats['mean'], crop_stats['std'])
        
        return {
            'current_price': current_price,
            'avg_price': crop_stats['mean'],
            'price_volatility': crop_stats['std'] / crop_stats['mean'],
            'trend': np.random.choice(self.price_trends, p=[0.3, 0.4, 0.3])
        }

    def predict_demand(self, crop: str, region: str) -> Dict:
        """Predict future demand for a crop in a specific region."""
        # This would use actual demand prediction models
        base_demand_scores = {
            'rice': 0.8,
            'wheat': 0.7,
            'corn': 0.75,
            'soybeans': 0.65
        }
        
        demand_score = base_demand_scores.get(crop.lower(), 0.5)
        
        return {
            'demand_level': np.random.choice(self.demand_levels, p=[0.2, 0.5, 0.3]),
            'demand_score': demand_score,
            'growth_potential': demand_score * np.random.uniform(0.8, 1.2)
        }

    def calculate_profitability(
        self,
        crop: str,
        region: str,
        farm_size: float
    ) -> Dict:
        """Calculate potential profitability for a crop."""
        price_analysis = self.analyze_price_trends(crop, region)
        demand_analysis = self.predict_demand(crop, region)
        
        # Basic yield estimates (tons per hectare)
        base_yields = {
            'rice': 4.5,
            'wheat': 3.0,
            'corn': 5.5,
            'soybeans': 2.8
        }
        
        estimated_yield = base_yields.get(crop.lower(), 3.0) * farm_size
        production_cost = estimated_yield * price_analysis['current_price'] * 0.4  # 40% of revenue
        
        return {
            'estimated_yield': estimated_yield,
            'production_cost': production_cost,
            'potential_revenue': estimated_yield * price_analysis['current_price'],
            'profit_margin': 0.6,  # 60% margin
            'roi': 1.5  # 150% return on investment
        }

    def get_market_analysis(
        self,
        crop: str,
        region: str,
        farm_size: float
    ) -> MarketTrend:
        """Generate comprehensive market analysis for a crop."""
        price_analysis = self.analyze_price_trends(crop, region)
        demand_analysis = self.predict_demand(crop, region)
        profitability = self.calculate_profitability(crop, region, farm_size)
        
        return MarketTrend(
            crop=crop,
            current_price=price_analysis['current_price'],
            predicted_price=price_analysis['current_price'] * 
                (1.1 if price_analysis['trend'] == 'Increasing' else 
                 0.9 if price_analysis['trend'] == 'Decreasing' else 1.0),
            demand_level=demand_analysis['demand_level'],
            price_trend=price_analysis['trend'],
            confidence_score=0.8  # This would be calculated based on model confidence
        )

    def generate_market_report(
        self,
        crops: List[str],
        region: str,
        farm_size: float
    ) -> List[Dict]:
        """Generate a comprehensive market report for multiple crops."""
        report = []
        
        for crop in crops:
            market_trend = self.get_market_analysis(crop, region, farm_size)
            profitability = self.calculate_profitability(crop, region, farm_size)
            
            report.append({
                'crop': crop,
                'market_trend': market_trend,
                'profitability': profitability,
                'recommendation_score': (
                    (profitability['roi'] * 0.4) +
                    (demand_analysis['demand_score'] * 0.3) +
                    (0.3 if market_trend.price_trend == 'Increasing' else 
                     0.2 if market_trend.price_trend == 'Stable' else 0.1)
                )
            })
        
        # Sort by recommendation score
        report.sort(key=lambda x: x['recommendation_score'], reverse=True)
        return report 