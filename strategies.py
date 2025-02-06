import pandas as pd
import numpy as np
import ta  # Technical Analysis library

def moving_average_strategy(data, short_window=10, long_window=50):
    """
    A simple moving average crossover strategy.
    - Buys when short MA crosses above long MA
    - Sells when short MA crosses below long MA
    """
    data["SMA_short"] = data["Close"].rolling(window=short_window).mean()
    data["SMA_long"] = data["Close"].rolling(window=long_window).mean()

    data["Signal"] = np.where(data["SMA_short"] > data["SMA_long"], 1, 0)
    data["Position"] = data["Signal"].diff()

    return data
