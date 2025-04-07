-- Create tables for the Sustainable Farming AI System

-- Farmers table
CREATE TABLE IF NOT EXISTS farmers (
    farmer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    farm_size REAL NOT NULL,
    soil_type TEXT NOT NULL,
    water_availability TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crops table
CREATE TABLE IF NOT EXISTS crops (
    crop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    water_requirement REAL NOT NULL,
    carbon_footprint REAL NOT NULL,
    soil_suitability TEXT NOT NULL,
    growth_period_days INTEGER NOT NULL
);

-- Market data table
CREATE TABLE IF NOT EXISTS market_data (
    market_id INTEGER PRIMARY KEY AUTOINCREMENT,
    crop_id INTEGER NOT NULL,
    region TEXT NOT NULL,
    price_per_kg REAL NOT NULL,
    demand_level TEXT NOT NULL,
    date_recorded DATE NOT NULL,
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id)
);

-- Farming recommendations table
CREATE TABLE IF NOT EXISTS recommendations (
    recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    farmer_id INTEGER NOT NULL,
    crop_id INTEGER NOT NULL,
    sustainability_score REAL NOT NULL,
    profitability_score REAL NOT NULL,
    water_efficiency_score REAL NOT NULL,
    recommendation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (farmer_id) REFERENCES farmers(farmer_id),
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id)
);

-- Historical farming data table
CREATE TABLE IF NOT EXISTS farming_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    farmer_id INTEGER NOT NULL,
    crop_id INTEGER NOT NULL,
    planting_date DATE NOT NULL,
    harvest_date DATE,
    yield_amount REAL,
    water_used REAL,
    carbon_emissions REAL,
    FOREIGN KEY (farmer_id) REFERENCES farmers(farmer_id),
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id)
); 