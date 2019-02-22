# Importing packages and creating aliases for the packages
import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

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

#save_sp500_tickers()

def get_data_from_yahoo(reload_sp500 = False):

    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
         with open("sp500tickers.pickle", "rb") as f:
             tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2009, 1, 1) # Start date
    end = dt.datetime(2018, 12, 31) # End date

    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()