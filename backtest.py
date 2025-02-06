import pandas as pd
import matplotlib.pyplot as plt
from strategies import moving_average_strategy

def load_historical_data(csv_file):
    data = pd.read_csv(csv_file, parse_dates=["Date"])
    data = data.sort_values("Date")
    return data

def backtest_strategy(data):
    strategy_data = moving_average_strategy(data)
    plt.figure(figsize=(12, 6))
    plt.plot(data["Date"], data["Close"], label="Price", color="black")
    plt.plot(data["Date"], strategy_data["SMA_short"], label="Short MA", color="blue")
    plt.plot(data["Date"], strategy_data["SMA_long"], label="Long MA", color="red")

    plt.legend()
    plt.title("Moving Average Crossover Strategy Backtest")
    plt.show()

if __name__ == "__main__":
    data = load_historical_data("btc_historical_data.csv")
    backtest_strategy(data)
