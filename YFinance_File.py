import yfinance as yf
import pandas as pd

def YahooData2returns(YahooData):

    prices = YahooData['Adj Close']
    pricevec = prices.values
    returns = pricevec[1:] / pricevec[:-1] - 1
    return returns

def get_stock_data(symbol):
    data = yf.download(symbol)
    prices = data['Adj Close']
    return prices

prices = get_stock_data('GS')
print(type(prices))
pricevec = prices.values


n = len(pricevec)
ratiovec = pricevec[1:n] / pricevec[:n-1]


def get_returns(pricevec):
    returns = pricevec[1:] / pricevec[:-1] - 1
    return returns


returns = get_returns(pricevec)
print(returns)
