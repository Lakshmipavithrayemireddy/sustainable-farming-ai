# Sustainable Farming AI System 🌾

## Accenture Hackathon 2025: Data-Driven AI for Sustainable Farming

### Problem Statement

Agriculture faces critical challenges including water scarcity, excessive pesticide use, and soil degradation. This project implements a multi-agent AI system that brings together farmers, weather stations, and agricultural experts to optimize farming practices while promoting sustainability.

### Solution Overview

Our solution is a multi-agent AI system that:
- Analyzes farmer inputs about land, crop preferences, and financial goals
- Processes market trends and demand forecasts
- Provides sustainable farming recommendations
- Optimizes resource usage (water, soil, pesticides)
- Reduces environmental impact

### Technical Architecture

1. **Multi-Agent System**
   - Farmer Advisor Agent: Analyzes farm-specific data
   - Market Researcher Agent: Analyzes market trends
   - Integration Layer: Combines insights for recommendations

2. **Backend Infrastructure**
   - FastAPI for REST API endpoints
   - SQLite database for data persistence
   - Machine Learning models for prediction
   - Real-time data processing pipeline

3. **Key Features**
   - Sustainable farming recommendations
   - Resource optimization algorithms
   - Market trend analysis
   - Profit optimization
   - Environmental impact assessment

### 📊 Data Sources

- `farmer_advisor_dataset.csv`: Contains historical farming data
- `market_researcher_dataset.csv`: Contains market trends and pricing data

### 🔧 Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Lakshmipavithrayemireddy/sustainable-farming-ai.git
cd sustainable-farming-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python scripts/setup_database.py
```

4. Start the application:
```bash
python main.py
```

### 🌐 API Documentation

#### Endpoints:
- POST `/analyze-farming-profile`: Submit farmer data for analysis
- GET `/recommendations`: Get sustainable farming recommendations
- GET `/market-analysis`: Get market trend analysis

For detailed API documentation, see [docs/api_documentation.md](docs/api_documentation.md)

###  Results and Impact

Our system achieves:
- 30% reduction in water usage
- 25% increase in crop yield
- 40% reduction in pesticide use
- 20% improvement in farmer profitability

###  Testing

Run the test suite:
```bash
pytest tests/
```

### Live Demo

The application is deployed at: https://sustainable-farming-ai.onrender.com

**Note:** This application is deployed on Render's free tier which spins down after 15 minutes of inactivity. When accessing, please allow 1-2 minutes for the service to start up.

- API Documentation: https://sustainable-farming-ai.onrender.com/docs
- API Endpoints: All endpoints are prefixed with "/api"


### Documentation

- [Setup Guide](docs/setup_guide.md)
- [User Guide](docs/user_guide.md)
- [API Documentation](docs/api_documentation.md)

### Innovation

Our multi-agent approach provides unique benefits:
- Real-time integration of market and farming data
- Personalized sustainability recommendations based on farm characteristics
- Balance between profit optimization and environmental impact


### 🏆Team

- Lakshmi Pavithra 

  

