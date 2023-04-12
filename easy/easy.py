import requests
import csv
from bs4 import BeautifulSoup as BS


URL = 'https://www.kivano.kg'

response = requests.get(URL)

soup = BS(response.text, 'html.parser')

def get_tel_nums():
    list_of_nums =[]

    new_list = []
    
    nums = (soup.find('span', id='phones').text)
    
    nums.strip()
    list_of_nums = nums.split('\n')
    for num in list_of_nums:
        num = num.replace('\r', '')
        num = num.strip()
        if num:
            new_list.append([num.replace(' ', '')])
    
    number = (soup.find('div', id='whatsapp').text)
    new_list.append([number.replace(' ', '')])
 

    with open('kivano.csv', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(new_list)




def get_price():
    cards = soup.find_all('div', {'class': 'product_box'})
    list_ = []
    for card in cards:
        product = card.find('div', {'class': 'product_title'}).text
    
        price = card.find('div', {'class': 'product_price'}).text.replace('\n', '').replace('  ','')
    
        link = URL + card.find('img').get('src')
  
        list_.append([product, price, link])


    with open('kivano.csv', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(list_)
    
    return list_


def start():
    get_tel_nums()
    get_price()


start()