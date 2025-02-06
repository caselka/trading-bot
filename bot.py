import requests

def get_crypto_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    print("Fetching live crypto price...")
    price = get_crypto_price()
    print(f"Current BTC Price: ${price['price']}")
