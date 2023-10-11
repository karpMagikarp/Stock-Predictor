import requests
api_key = 'YOUR_API_KEY'
symbols = ['UBER']
stock_prices = []
for symbol in symbols:
    response = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}')
    data = response.json()
    try:
        low_price = data['Global Quote']['04. low']
        high_price = data['Global Quote']['03. high']
        current_price = data['Global Quote']['05. price']
        stock_prices.append([symbol, low_price, high_price, current_price])
    except KeyError:
        print("Key Error")

print(stock_prices)