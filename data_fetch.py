import requests
import private
from moralis import evm_api

#CoinGeko api import
headers = {"accept": "application/json","x-cg-demo-api-key": private.gekco_api_key}
root_url = "https://api.coingecko.com/api/v3"

#Moralis API
Moralis_api_key = private.moralis_api_key

#Get wallet history
def get_wallet_history(address: str, chain: str = "eth", order: str = "DESC", limit: int = 10):
    params = {
        "address": address,
        "chain": chain,
        "order": order,
        "limit": limit,
    }
    return evm_api.wallets.get_wallet_history(api_key= Moralis_api_key , params=params)

#Coingecko
def get_coin_data(coin):
    url = f"{root_url}/simple/price?vs_currencies=usd&ids={coin}&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true"
    response = requests.get(url, headers=headers)
    print(response.text)

coin_input = input("Enter coin name: ")
get_coin_data(coin_input)

wallet_history_fetch = input("Enter wallet address: ")
print(get_wallet_history(wallet_history_fetch))