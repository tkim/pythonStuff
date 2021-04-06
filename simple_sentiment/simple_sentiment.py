import nltk
from textblob import TextBlob
from newspaper import Article

url = 'https://www.cnbc.com/2021/04/05/gamestop-plummets-after-reddit-favorite-plans-1-billion-stock-sale.html'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
# text = article.text
print(text)

# create text blob object
blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)