import datetime as dt 
import matplotlib as plt 
import pandas_datareader as web

# Full list of tickers
tickers = ['UVXY', 'AMZN', 'BTC', 'ETH']
amounts = [900, 1, 1, 1]
prices = []
total = []

# Define time frame
start = dt.datetime(2020,1,1)
# end = dt.datetime.now()
end = dt.datetime(2020,7,1)

for ticker in tickers:
    df = web.DataReader(ticker, 'yahoo', start, end)
    price = df[-1:]['Close'][0]
    prices.append(price)
    index = tickers.index(ticker)
    total.append(price * amounts[index])

print(prices)
print(total)


