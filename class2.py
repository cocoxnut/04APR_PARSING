import csv

from bs4 import BeautifulSoup
import requests
import csv
CSV = 'sulpak.csv'
URL = 'https://www.sulpak.kg/f/noutbuki'
HOST = 'https://www.sulpak.kg'
def get_html(URL, params = ''):
    r = requests.get(URL, params = params, verify=False)
    return r

def get_content(html):
    soup = BeautifulSoup(html)
    items = soup.find_all('div', class_ = 'goods-tiles')
    comps = []
    for item in items:
        comps.append({
            'name': item.find('div', class_='title'),
            'price': item.find('div', class_='price'),
            'link': HOST + item.find('div', class_='goods-photo').find('a').get('href'),
            'image' : item.find('img', class_ = 'image-size-cls').get('src')
        })
    return comps
def save(items, path):
    with open(path, 'w') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['name', 'link', 'image', 'price'])
        for item in items:
            writer.writerow([item['name'], item['link'], item['image'], item['price']])
#save(get_content(get_html(URL)), CSV)

def pagination():
    PAGINATION = input('pages ? :')
    PAGINATION = int(PAGINATION.strip())
    items = []
    html = get_html(URL)
    if html.status_code == 200
        for page in range(1, PAGINATION +1):
            print(f'page {page} is done')
            html = get_html(URL, params = {'pages' : page})
            items.extend(get_content(html.text))
        save(items, CSV)
        print('parsing is done')
    else:
        print('parsing is break')
pagination()