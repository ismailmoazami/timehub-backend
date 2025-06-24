from web3 import Web3
import os 
import dotenv
import json

INFURA_URL = os.getenv("INFURA_URL")
factory_contract_address = os.getenv("factory_contract_address")

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

current_dir = os.path.dirname(__file__)
factory_abi_path = os.path.join(current_dir, "factory_abi.json")
time_market_abi_path = os.path.join(current_dir, "time_market_abi.json")

with open(factory_abi_path, "r") as file:
    file_data = json.load(file)
    factory_abi = file_data['abi']

with open(time_market_abi_path, "r") as file:
    file_data = json.load(file)
    time_market_abi = file_data['abi']

def getContract(address, abi):
    return w3.eth.contract(
            address=address,
            abi=abi
    )

def getTimeMarketContract(address):
    return getContract(address, time_market_abi)

contract = getContract(factory_contract_address, factory_abi)
