from .eth import w3, getTimeMarketContract

ETH_PRICE = 2500

async def getPrice(address: str):
    contract = getTimeMarketContract(address)
    price_in_eth = contract.functions.getCurrentPrice().call()

    price_in_usd = (price_in_eth / (10 ** 18)) * ETH_PRICE

    return round(price_in_usd, 4) 