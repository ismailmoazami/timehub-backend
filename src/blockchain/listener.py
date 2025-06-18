from .eth import contract, w3
import time 
from sqlmodel import Session, select
from database import engine 
from models import TimeMarket

SLEEP_TIME: int = 10 # seconds

def listen_to_events():
    
    print("📡 Event listener started...")
    last_checked_block = w3.eth.block_number
    
    while True:
        
        try:
            current_block = w3.eth.block_number 

            events = contract.events.NewTimeTokenCreated().get_logs(
                from_block=last_checked_block + 1,
                to_block=current_block
            )

            with Session(engine) as session:
                token_address = event["args"]["timeToken"] 
                creator_address = event["args"]["creator"]
                for event in events:
                    exists = session.exec(select(TimeMarket).where(TimeMarket.address == token_address)).first()
                    if exists:
                        continue
                    time_market = TimeMarket(
                        name="unknown",
                        address=token_address,
                        creator_address=creator_address
                    )
                    session.add(time_market)
                    session.commit()
                print(f"Time Market added : {event["args"]["timeToken"]}")
                

            last_checked_block = current_block 

        except Exception as e:
            print(f"Error occured: {e}")
        
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    listen_to_events()