import csv
import requests
from bs4 import BeautifulSoup


def parse():
    url = 'https://habr.com/ru/feed/page2/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    news = soup.find_all('h2', class_='tm-title tm-title_h2')

    news_links = [n.find('a').get('href') for n in news]
    news_text = [n.text.strip() for n in news]

    with open('news.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link'])
        for text, link in zip(news_text, news_links):
            full_link = 'https://habr.com' + link
            writer.writerow([text, full_link])


if __name__ == '__main__':
    parse()