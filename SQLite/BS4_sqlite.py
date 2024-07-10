import sqlite3
import requests
from bs4 import BeautifulSoup


def parse():
    url = 'https://habr.com/ru/feed/page1/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    news = soup.find_all('h2', class_='tm-title tm-title_h2')

    news_links = [n.find('a').get('href') for n in news]
    news_text = [n.text.strip() for n in news]

    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        for link, text in zip(news_links, news_text):
            full_link = 'https://habr.com' + link
            query = """CREATE TABLE IF NOT EXISTS news(name TEXT, link TEXT)"""
            cursor.execute(query)
            query = """INSERT INTO news(name, link) VALUES (?, ?)"""
            cursor.execute(query, (text, full_link))

            db.commit()


if __name__ == '__main__':
    parse()
