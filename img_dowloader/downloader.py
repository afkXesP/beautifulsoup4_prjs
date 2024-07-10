import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def download_img(url, folder):
    r = requests.get(url)
    if r.status_code == 200:
        filename = os.path.join(folder, url.split('/')[-1])
        with open(filename, 'wb') as file:
            file.write(r.content)
        print(f'Downloaded {url} to {filename}')
    else:
        print(f'Failed to download {url}')


def parse():
    url = ""
    folder = 'downloaded_images'

    if not os.path.exists(folder):
        os.mkdir(folder)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    img_tags = [i.find('img') for i in soup.find_all('div', class_='image')]

    for img in img_tags:
        img_url = img.get('src')

        if not img_url:
            continue

        img_url = urljoin(url, img_url)
        download_img(img_url, folder)


if __name__ == '__main__':
    parse()
