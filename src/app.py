from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from sqlmodel import Session, select
from threading import Thread
from contextlib import asynccontextmanager
from models import (
    TimeMarket
)
from routers import router 
from blockchain.listener import listen_to_events
from database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    create_db_and_tables()

    thread = Thread(target=listen_to_events, daemon=True)
    thread.start()

    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)