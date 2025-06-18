from sqlmodel import create_engine, SQLModel
import os 
import dotenv
from models import (
    TimeMarket
)

dotenv.load_dotenv()

username = os.getenv("username")
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")
database = os.getenv("database")

DATABASE_URL  = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    print("Creating database and tables....")
    create_db_and_tables()
    print("Database and tables created successfully")