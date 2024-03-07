import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import json


def analyze_stock(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    
    ticker = config['ticker']
    start_date = config['start_date']
    end_date = config['end_date']


    data = yf.download(ticker, start=start_date, end=end_date)
    

    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()


    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', alpha=0.5)
    plt.plot(data['MA50'], label='50-Day Moving Average', alpha=0.75)
    plt.plot(data['MA200'], label='200-Day Moving Average', alpha=0.75)
    plt.title(f'{ticker} Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


analyze_stock('config.json')
