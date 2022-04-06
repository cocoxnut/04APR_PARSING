from bs4 import BeautifulSoup
import requests

URL = requests.get('https://sulpak.kg/f/smart_chasiy', verify=False).text
soup = BeautifulSoup(URL)
data = soup.find('ul', class_ = 'goods-container').find_all('li', class_ = 'tile-container')
name = []
price = []
for i in data:
    title = i.find('li', class_ = 'tile-container')
    money = i.find('div', class_ = 'price')
    name.append(title)
    price.append(money)
print(name, price)
