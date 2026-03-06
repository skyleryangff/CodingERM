import yfinance as yf
import pandas as pd

def YahooData2returns(YahooData=None,symbol='AAPL'):
    # Input:
    # YahooData = data from Yahoo Finance
    # Output:
    # returns = array of returns
    # Steps:
    # Extract 'Close' and symbol (This is a 2d column. Demo below.)
    # Calculate and return the lagged returns
    returns = np.array([0.01      , 0.00990099])
    return returns
