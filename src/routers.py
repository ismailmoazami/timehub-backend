from fastapi import APIRouter
from models import TimeMarket, User
from sqlmodel import Session, select
from database import engine 
from pydantic import BaseModel

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
    
@router.get("/users")
def getUsers():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users

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