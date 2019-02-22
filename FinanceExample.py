# Importing packages and creating aliases for the packages
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot') # Style type

#start = dt.datetime(2009, 1, 1) # Start date
#end = dt.datetime(2018, 12, 31) # End date
#df = web.DataReader('TSLA', 'yahoo', start, end) # Set up data frame using Tesla ticker
#print(df.head()) # Print first five rows in data frame
#print(df.tail()) # Print last five rows in data frame

#df.to_csv('tsla.csv') # Data frame to save Telsa historical data to .csv file

#df = pd.read_csv('tsla.csv') # Read .csv file in data frame

df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0) # Read .csv file in data frame with dates parsed and columns

#print(df.head()) # Print first five rows in tsla.csv file
#print(df[['Open', 'High']].head()) # Print only Open and High of first five rows of tsla.csv file

#df.plot() # Plot graph of Tesla data
#df['Adj Close'].plot() # Plot graph of Tesla Adjusted Close data
#plt.show() # Show graph of Tesla data

#df['100ma'] = df['Adj Close'].rolling(window = 100).mean() # Data frame for 100 day Moving Average based on Adjusted Close
#df.dropna(inplace = True) # Modify data frame in place as True
#print(df.head()) # Print first five rows in data frame including Moving Average
#print(df.tail()) # Print last five rows in data frame including Moving Average

#df['100ma'] = df['Adj Close'].rolling(window = 100, min_periods = 0).mean() # Data frame for 100 day Moving Average based on Adjusted Close with minimum periods
#print(df.head()) # Print first five rows in data frame including Moving Average with minimum periods
#print(df.tail()) # Print last five rows in data frame including Moving Average with minimum periods

df_ohlc = df['Adj Close'].resample('10D').ohlc() # Data frame for Adjusted Close resampled over 10 days for open, high, low, and close
df_volume = df['Volume'].resample('10D').sum() # Data frame for Volume resampled over 10 days for sum
df_ohlc.reset_index(inplace = True)
#print(df_ohlc.head())
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan = 5, colspan = 1) # Create subplot ax1
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan = 1, colspan = 1, sharex = ax1) # Create subplot ax2 and share with ax1
ax1.xaxis_date() # Take end dates and displays as nice dates

candlestick_ohlc(ax1, df_ohlc.values, width = 2, colorup = 'g') # Takes ax1 and creates values
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0) # Fills values x from 0 to y
plt.show()

#ax1.plot(df.index, df['Adj Close']) # Plot Adjusted Close line graph in red
#ax1.plot(df.index, df['100ma']) # Plot 100 Moving Average line graph in blue
#ax2.bar(df.index, df['Volume']) # Plot Volume bar graph
#plt.show() # Plot line and bar graphs
