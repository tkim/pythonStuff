import datetime as dt 
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

# Define time frame
start = dt.datetime(2020,1,1)
# end = dt.datetime.now()
end = dt.datetime(2020,7,1)

# Load the data
data = web.DataReader('UVXY','yahoo', start, end)

# print(data.columns)
# print(data)

# Restructure Data
data = data[['Open', 'High', 'Low', 'Close']]

data.reset_index(inplace=True)
# Convert date into numbers
data['Date'] = data['Date'].map(mdates.date2num)

# print(data.head())

# Visualization
ax = plt.subplot()
# Create grid
ax.grid(True)
# Makesure it is below the data points
ax.set_axisbelow(True)
# Set title
ax.set_title('UVXY 2020 - Now', color='white')
# Set background to black
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width=1.5, colorup='#00ff00')
plt.show()