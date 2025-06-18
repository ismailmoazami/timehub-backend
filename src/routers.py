from fastapi import APIRouter
from models import TimeMarket

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the Timehub API!"}

@router.get("/time_markets")
def getTimeMarkets():
    with Session(engine) as session: 
        time_markets = session.exec(select(TimeMarket)).all()
        return time_markets

@router.post("/time_markets")
def createTimeMarkets(timemarket: TimeMarket):
    with Session(engine) as session:
        session.add(timemarket)
        session.commit()
        session.refresh(timemarket)
    return timemarket 

@router.get("/time_markets/{username}")
def getTimeMarket(username):
    with Session(engine) as session:
        timemarket = session.exec(select(TimeMarket).where(TimeMarket.name == username)).all()
        return timemarket