import requests
import private

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": private.api_key
}

root_url = "https://api.coingecko.com/api/v3"

def get_coin_data(coin):
    url = f"{root_url}/simple/price?vs_currencies=usd&ids={coin}&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true"
    response = requests.get(url, headers=headers)
    print(response.text)

coin_input = input("Enter coin name: ")
get_coin_data(coin_input)