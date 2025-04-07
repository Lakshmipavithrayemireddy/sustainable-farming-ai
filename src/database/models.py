from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Farmer(Base):
    __tablename__ = 'farmers'
    
    farmer_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    farm_size = Column(Float, nullable=False)
    soil_type = Column(String(50), nullable=False)
    water_availability = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    recommendations = relationship("Recommendation", back_populates="farmer")
    farming_history = relationship("FarmingHistory", back_populates="farmer")

class Crop(Base):
    __tablename__ = 'crops'
    
    crop_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    water_requirement = Column(Float, nullable=False)
    carbon_footprint = Column(Float, nullable=False)
    soil_suitability = Column(String(100), nullable=False)
    growth_period_days = Column(Integer, nullable=False)
    
    market_data = relationship("MarketData", back_populates="crop")
    recommendations = relationship("Recommendation", back_populates="crop")
    farming_history = relationship("FarmingHistory", back_populates="crop")

class MarketData(Base):
    __tablename__ = 'market_data'
    
    market_id = Column(Integer, primary_key=True)
    crop_id = Column(Integer, ForeignKey('crops.crop_id'), nullable=False)
    region = Column(String(100), nullable=False)
    price_per_kg = Column(Float, nullable=False)
    demand_level = Column(String(50), nullable=False)
    date_recorded = Column(DateTime, nullable=False)
    
    crop = relationship("Crop", back_populates="market_data")

class Recommendation(Base):
    __tablename__ = 'recommendations'
    
    recommendation_id = Column(Integer, primary_key=True)
    farmer_id = Column(Integer, ForeignKey('farmers.farmer_id'), nullable=False)
    crop_id = Column(Integer, ForeignKey('crops.crop_id'), nullable=False)
    sustainability_score = Column(Float, nullable=False)
    profitability_score = Column(Float, nullable=False)
    water_efficiency_score = Column(Float, nullable=False)
    recommendation_date = Column(DateTime, default=datetime.utcnow)
    details = Column(Text)  # JSON string containing detailed recommendations
    
    farmer = relationship("Farmer", back_populates="recommendations")
    crop = relationship("Crop", back_populates="recommendations")

class FarmingHistory(Base):
    __tablename__ = 'farming_history'
    
    history_id = Column(Integer, primary_key=True)
    farmer_id = Column(Integer, ForeignKey('farmers.farmer_id'), nullable=False)
    crop_id = Column(Integer, ForeignKey('crops.crop_id'), nullable=False)
    planting_date = Column(DateTime, nullable=False)
    harvest_date = Column(DateTime)
    yield_amount = Column(Float)
    water_used = Column(Float)
    carbon_emissions = Column(Float)
    notes = Column(Text)
    
    farmer = relationship("Farmer", back_populates="farming_history")
    crop = relationship("Crop", back_populates="farming_history") 