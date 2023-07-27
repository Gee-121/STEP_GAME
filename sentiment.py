import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')
url = 'https://www.apple.com/'
#this code bassically shows you stocks and info on stuff
article = Article(url)
article.download()
article.parse()
article.nlp()
text = article.summary
print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)
