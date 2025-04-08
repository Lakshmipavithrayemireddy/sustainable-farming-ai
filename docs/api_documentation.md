# API Documentation for Sustainable Farming AI System

## Base URL
All endpoints are prefixed with: `/api`

## Authentication
Currently, the API does not require authentication.

## Endpoints

### 1. Create Farmer Profile
**POST** `/api/farmers/`

Creates a new farmer profile in the system.

**Request Body:**
```json
{
  "name": "John Smith",
  "location": "Karnataka",
  "farm_size": 10.5,
  "soil_type": "loamy",
  "water_availability": "medium",
  "preferred_crops": ["rice", "wheat"],
  "budget": 50000
}
```

**Response:**
```json
{
  "farmer_id": 1,
  "message": "Farmer profile created successfully"
}
```

### 2. Get Recommendations
**GET** `/api/recommendations/{farmer_id}`

Retrieves sustainable farming recommendations for a specific farmer.

**Parameters:**
- `farmer_id`: The ID of the farmer (integer)

**Response:**
```json
{
  "farmer_id": 1,
  "recommendations": [
    {
      "crop": "rice",
      "sustainability_score": 0.85,
      "water_requirement": 1500,
      "soil_compatibility": 0.9,
      "market_analysis": {
        "price_trend": "Increasing",
        "demand_level": "High"
      },
      "overall_score": 0.88
    }
  ],
  "timestamp": "2024-04-08T15:30:00Z"
}
```

### 3. Get Market Analysis
**GET** `/api/market-analysis/{region}`

Provides market trend analysis for crops in a specific region.

**Parameters:**
- `region`: Region name (string)
- `crops`: Optional comma-separated list of crops (string)

**Response:**
```json
{
  "region": "Karnataka",
  "market_analysis": [
    {
      "crop": "rice",
      "market_trend": {
        "current_price": 380.5,
        "predicted_price": 410.2,
        "demand_level": "High",
        "price_trend": "Increasing"
      },
      "profitability": {
        "roi": 1.5,
        "profit_margin": 0.6
      }
    }
  ],
  "timestamp": "2024-04-08T15:30:00Z"
}
```

### 4. Get Sustainable Practices
**GET** `/api/sustainable-practices/{farmer_id}/{crop}`

Provides sustainable farming practices for a specific crop.

**Parameters:**
- `farmer_id`: The ID of the farmer (integer)
- `crop`: Crop name (string)

**Response:**
```json
{
  "farmer_id": 1,
  "crop": "rice",
  "sustainable_practices": [
    {
      "practice": "Drip irrigation",
      "benefit": "Reduces water consumption by up to 40%",
      "cost_impact": 0.15,
      "sustainability_impact": 0.4
    }
  ],
  "timestamp": "2024-04-08T15:30:00Z"
}
```

## Error Responses
All endpoints return standard HTTP status codes:
- 200: Success
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error

Error response format:
```json
{
  "detail": "Error message description"
}
```
```

