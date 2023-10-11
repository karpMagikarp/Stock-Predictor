import yfinance as yf
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import requests
import plotly
import plotly.io as pio
import requests

# Replace YOUR_API_KEY with your Alpha Vantage API key
api_key = 'YOUR_API_KEY'


def get_stock_data(symbol):
    # Make a GET request to the Alpha Vantage API to retrieve the stock data for the given symbol
    response = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}')

    # Parse the response JSON to retrieve the stock data
    data = response.json()
    stock_data = {
        'symbol': symbol,
        'low': data['Global Quote']['04. low'],
        'high': data['Global Quote']['03. high'],
        'price': data['Global Quote']['05. price']
    }

    return stock_data


def msft():
    data = yf.download(tickers='MSFT', period='1d', interval='1m')
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'], name='market data'))
    fig.update_layout(
        title='Microsoft live share price evolution',
        yaxis_title='Stock Price (USD per Shares)')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label='15m', step='minute', stepmode='backward'),
                dict(count=45, label='45m', step='minute', stepmode='backward'),
                dict(count=1, label='HTD', step='hour', stepmode='todate'),
                dict(count=3, label='3h', step='hour', stepmode='backward'),
                dict(step='all')
            ])

        )
    )
    #plotly.offline.plot(fig, filename='templates/msft.html', config={'displayModeBar': False})
    pio.write_image(fig, "D:\programing\year 2 project\static\css\image\msft.png")


def google():
    data = yf.download(tickers='GOOGL', period='1d', interval='1m')
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'], name='market data'))
    fig.update_layout(
        title='Google live share price evolution',
        yaxis_title='Stock Price (USD per Shares)')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label='15m', step='minute', stepmode='backward'),
                dict(count=45, label='45m', step='minute', stepmode='backward'),
                dict(count=1, label='HTD', step='hour', stepmode='todate'),
                dict(count=3, label='3h', step='hour', stepmode='backward'),
                dict(step='all')
            ])

        )
    )
    #plotly.offline.plot(fig, filename='templates/google.html', config={'displayModeBar': False})
    pio.write_image(fig, "D:\programing\year 2 project\static\css\image\google.png")


def uber():
    data = yf.download(tickers='UBER', period='1d', interval='1m')
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'], name='market data'))
    fig.update_layout(
        title='Uber live share price evolution',
        yaxis_title='Stock Price (USD per Shares)')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label='15m', step='minute', stepmode='backward'),
                dict(count=45, label='45m', step='minute', stepmode='backward'),
                dict(count=1, label='HTD', step='hour', stepmode='todate'),
                dict(count=3, label='1d', step='day', stepmode='backward'),
                dict(step='all')
            ])

        )
    )
    
    #plotly.offline.plot(fig, filename='templates/uber.html', config={'displayModeBar': False})
    pio.write_image(fig, "D:/programing/year 2 project/static/css/image/uber.png")

