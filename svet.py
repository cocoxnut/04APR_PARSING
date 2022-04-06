from bs4 import BeautifulSoup
import requests

URL = 'https://svetofor.info/noutbuki-planshety-bukridery/apple-macbook/'
r = requests.get(URL).text
soup = BeautifulSoup(r)
price = soup.find('span',class_='ty-price-num')
print(price.text)