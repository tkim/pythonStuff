import datetime as dt 
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Define time frame
start = dt.datetime(2017,1,1)
end = dt.datetime.now()

# Load the data
data = web.DataReader('UVXY','yahoo', start, end)

print(data.columns)
print(data)


