from sqlmodel import SQLModel, Field, create_engine

class TimeMarket(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str 
    address: str 
    creator_address: str 
    
