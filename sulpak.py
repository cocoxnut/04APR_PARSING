from bs4 import BeautifulSoup
import requests
CSV = 'sulpak.csv'
HOST = 'https://www.sulpak.kg'
URL = 'https://www.sulpak.kg/f/noutbuki'
HEADERS = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

r = requests.get(URL).text
soup = BeautifulSoup(r)
price = soup.find('div',class_='price')
print(price)