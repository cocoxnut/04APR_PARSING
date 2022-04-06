from bs4 import BeautifulSoup
import requests
URL = requests.get('https://www.kivano.kg/mobilnye-telefony').text
soup = BeautifulSoup(URL,'lxml')
#data = soup.find('div', class_ = 'list-view').find('div', class_ = 'listbox_title oh')
#price = soup.find('div', class_ = 'listbox_price text-center')
data_all = soup.find('div', class_ = 'list-view').find_all('div', class_ = 'item product_listbox oh')
name = []
price = []
for i in data_all:
    title = i.find('div', class_ = 'listbox_title oh')
    money = i.find('div', class_ = 'listbox_price text-center')
    name.append(title.text)
    price.append(money.text)
print(name, price)
