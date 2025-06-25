# Timehub Backend

Timehub is a blockchain-based platform for managing and tracking time markets. This backend is built using FastAPI and integrates with Ethereum smart contracts to provide real-time data and functionality.

## Features
- **Event Listener**: Listens to blockchain events for new time tokens.
- **API Endpoints**: Provides RESTful APIs for managing users, time markets, and retrieving data.
- **Database Integration**: Uses SQLModel for database operations.
- **Local Network Access**: Can be accessed by front-end developers on the same network.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/timehub-backend.git
   cd timehub-backend

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

3. Run the FastAPI server:
   ```bash
   uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload