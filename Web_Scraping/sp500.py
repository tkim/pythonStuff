import requests
from bs4 import BeautifulSoup

import csv
import pickle
import pandas as pd

html = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

# print(html.text)
src = html.content
soup = BeautifulSoup(src, 'lxml')

tickers = []

table = soup.find('table', {'class': 'wikitable sortable'})
rows = table.findAll('tr')[1:]
for row in rows:
    ticker = row.findAll('td')[0].text
    tickers.append(ticker[:-1])

print(tickers)

with open('snp500.pickle', 'wb') as f:
     pickle.dump(tickers, f)

with open('snp500.pickle', 'rb') as f:
    object = pickle.load(f)

df = pd.DataFrame(object)
df.to_csv(r'snp500.csv')



