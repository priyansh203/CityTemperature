import requests,json


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GAIL&interval=5min&outputsize=full&apikey=ETNAPCYY1REJLCHJ'

r = requests.get(url)
data = r.json()

print(data)