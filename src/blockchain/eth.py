from web3 import Web3
import os 
import dotenv
import json

INFURA_URL = os.getenv("INFURA_URL")
factory_contract_address = os.getenv("factory_contract_address")

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

current_dir = os.path.dirname(__file__)
factory_abi_path = os.path.join(current_dir, "factory_abi.json")

with open(factory_abi_path, "r") as file:
    file_data = json.load(file)
    abi = file_data['abi']

contract = w3.eth.contract(
    address=factory_contract_address,
    abi=abi
)
