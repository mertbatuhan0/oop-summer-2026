import requests

news = requests.get('https://www.trthaber.com/haber/gundem/')

print(news.text)