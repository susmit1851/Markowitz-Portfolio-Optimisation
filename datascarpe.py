import yfinance as yf
import pandas as pd
import os

nifty50_stocks = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 'ICICIBANK.NS',
                  'KOTAKBANK.NS', 'HINDUNILVR.NS', 'BHARTIARTL.NS', 'ITC.NS', 'LT.NS']

def download_stock_data(stock_list, start_date='2010-01-01', end_date='2024-01-01'):
    stock_data = {}
    for stock in stock_list:
        data = yf.download(stock, start=start_date, end=end_date)
        stock_data[stock] = data
        print(f'Downloaded data for {stock}')
    return stock_data

nifty50_data = download_stock_data(nifty50_stocks)
for stock, data in nifty50_data.items():
    data.to_csv(os.path.join("data", f'{stock}_historical_data.csv'))

print('Data download complete.')

