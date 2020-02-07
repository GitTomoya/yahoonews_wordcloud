import requests
from bs4 import BeautifulSoup

#カテゴリ一覧
urlList = ['https://news.yahoo.co.jp',
    'https://news.yahoo.co.jp/categories/domestic',
    'https://news.yahoo.co.jp/categories/world',
    'https://news.yahoo.co.jp/categories/business',
    'https://news.yahoo.co.jp/categories/entertainment',
    'https://news.yahoo.co.jp/categories/sports',
    'https://news.yahoo.co.jp/categories/it',
    'https://news.yahoo.co.jp/categories/science',
    'https://news.yahoo.co.jp/categories/life',
    'https://news.yahoo.co.jp/categories/local']

def TitleText():
    text = []

    for url in urlList:
        html = requests.get(url)
        news = BeautifulSoup(html.content, "html.parser")

        for i in range(1, 9):
            for title in news.select("li.topicsListItem:nth-child(" + str(i) + ")"):
                text.append(title.getText())
                print(title.getText())
    
    return str(text)