from sqlmodel import SQLModel, Field, create_engine

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    wallet_address: str = Field(index=True, unique=True)
    x: str | None = None 

class TimeMarket(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True) 
    address: str | None = Field(index=True, unique=True)
    migrated: bool = Field(default=False) 
    image: str | None = None 
    user_id: int = Field(foreign_key="user.id", unique=True)
