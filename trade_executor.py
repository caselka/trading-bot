import ccxt

exchange = ccxt.binance({
    "apiKey": "your_api_key",
    "secret": "your_api_secret"
})

def place_order(symbol, side, amount, price):
    order = exchange.create_limit_order(symbol, side, amount, price)
    return order

if __name__ == "__main__":
    # Example: Buy 0.01 BTC at $30,000
    order = place_order("BTC/USDT", "buy", 0.01, 30000)
    print("Trade executed:", order)
