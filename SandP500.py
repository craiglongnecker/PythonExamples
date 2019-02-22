# Importing packages and creating aliases for the packages
import bs4 as bs
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

style.use('ggplot') # Style type

def save_sp500_tickers(): # Create save_sp500_tickers function
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies') # Built-in module response
    soup = bs.BeautifulSoup(resp.text, "lxml") # Call BeautifulSoup class
    table = soup.find('table', {'class': 'wikitable sortable'}) # Soup.find built-in method
    tickers = [] # Create empty tickers list
    for row in table.findAll('tr') [1:]: # For loop
        ticker = row.findAll('td') [1].text
        tickers.append(ticker) # Append object to the end of the list

    with open("sp500tickers.pickle", "wb") as f: # Read file with pickle.dump
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

#save_sp500_tickers() # Run save_sp500_tickers() function

def get_data_from_yahoo(reload_sp500 = False): # Create get_data_from_yahoo function

    if reload_sp500: # If statement
        tickers = save_sp500_tickers()
    else: # Else statement
         with open("sp500tickers.pickle", "rb") as f: # read file with pickle.load
             tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'): # if statement
        os.makedirs('stock_dfs')

    start = dt.datetime(2009, 1, 1) # Start date
    end = dt.datetime(2018, 12, 31) # End date

    for ticker in tickers: # For loop
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)): # If not statement to create .csv files for each S&P 500 company
            df = web.DataReader(ticker, 'yahoo', start, end) # Set up data frame using S&P 500
            df.to_csv('stock_dfs/{}.csv'.format(ticker)) # Create .csv file for each S&P 500 company
        else: # Else statement
            print('Already have {}'.format(ticker))

#get_data_from_yahoo() # Run get_data_from_yahoo() function

def compile_data(): # Create compile_data function
    with open("sp500tickers.pickle", "rb") as f: # read file with pickle.load
        tickers = pickle.load(f)

    main_df = pd.DataFrame() # Main data frame

    for count, ticker in enumerate(tickers): # For loop
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker)) # Read each S&P 500 company .csv file
        df.set_index('Date', inplace = True)
        df.rename(columns = {'Adj Close': ticker}, inplace = True) # Rename Adjusted Close to ticker
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace = True) # Set up columns

        if main_df.empty: # If statement
            main_df = df
        else: # Else statement
            main_df = main_df.join(df, how = 'outer')

        if count % 10 == 0: # If statement counting using remainder of 10
            print(count)

    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv') # Create sp500_joined_closes.csv file

#compile_data() # Run compile_data function

def visualize_data(): # Create visualize_data function
    df = pd.read_csv('sp500_joined_closes.csv')
    #df['AAPL'].plot() # Plot Apple
    #plt.show() # Show graph of Apple
    df_corr = df.corr() # Create correlation table
    print(df_corr.head())
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Create custom correlation graph
    heatmap = ax.pcolor(data, cmap = plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor = False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor = False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    
    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation = 90)
    heatmap.set_clim(-1, 1)
    plt.tight_layout()
    plt.show() # Show correlation graph

visualize_data() # Run visualize_data function