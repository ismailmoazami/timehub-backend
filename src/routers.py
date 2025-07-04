from fastapi import APIRouter
from models import TimeMarket, User
from sqlmodel import Session, select
from database import engine 
from pydantic import BaseModel
from blockchain.helpers import getPrice 
from fastapi.responses import JSONResponse

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
    
@router.put("/time_markets/{address}")
def updateTimeMarketByAddress(address, updated_market: dict):
    with Session(engine) as session:
        market = session.exec(select(TimeMarket).where(TimeMarket.address == address)).first()
        
        for key, value in updated_market.items():
            setattr(market, key, value)
        
        session.add(market)
        session.commit()
        session.refresh(market)
        return market 
    
@router.get("/users")
def getUsers():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users

@router.get("/users/{address}")
def getUser(address: str):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.wallet_address == address)).first()
        if user is None:
            return JSONResponse(status_code=404, content={"message": "User not found"})
    return user
        

@router.post("/users")
def addUser(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)   
    return user 

@router.put("/users/{user_id}")
def updateUser(user_id, updated_user: dict):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.id == user_id)).first()

        for key, value in updated_user.items():
            setattr(user, key, value)
        
        session.add(user)
        session.commit()
        session.refresh(user)
        return user 

@router.get("/time_markets_data")
async def getTimeMarketsData():
    with Session(engine) as session:
        response = []
        timeMarkets = session.exec(select(TimeMarket)).all()
        
        for timeMarket in timeMarkets:
            time_market_price = await getPrice(timeMarket.address)
            image = timeMarket.image
            user = session.exec(select(User).where(User.id == timeMarket.user_id)).first()
            name = user.name
            x = user.x

            response.append({
                "name": name,
                "image": image,
                "price": time_market_price,
                "x": x
            })
        return response 

@router.get("/time_market_data/{xHandle}")
async def getTimeMarketData(xHandle: str):
    
    with Session(engine) as session:
        user = session.exec(select(User).where(User.x == xHandle)).first()
        time_market = session.exec(select(TimeMarket).where(TimeMarket.user_id == user.id)).first()
        image = time_market.image 
        time_market_price = await getPrice(time_market.address)
        name = user.name 
        address = time_market.address

    return({
        "name": name,
        "image": image,
        "price": time_market_price,
        "address": address
    })
    
