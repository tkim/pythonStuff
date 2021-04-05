import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf 
import datetime as dt 

crypto = "BTC"
currency = "USD"

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

# Pandas DataReader data source options 
# yahoo, google, fred (St. Louise Fed), famafrench (Kenneth French's data library)
# World bank  
# https://pandas.pydata.org/pandas-docs/version/0.18.1/remote_data.html#remote-data-fred

data = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)

# for creating multiple currency charts
btc = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
eth = web.DataReader(f"ETH-{currency}", "yahoo", start, end)

# to make the chart logrithimic
plt.yscale("log")

# print(data)

# basic line chart on Close
# plt.plot(data['Close'])
# plt.show()

# plot candlestick 
# mpf.plot(data, type="candle", volume=True, style="yahoo")  

# for multiple currency charts
plt.plot(btc['Close'], label="BTC")
plt.plot(eth['Close'], label="ETH")
plt.legend(loc="upper left")
plt.show()