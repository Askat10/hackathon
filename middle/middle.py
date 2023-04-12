import requests
import csv
from bs4 import BeautifulSoup as BS

for i in range(1, 11):

    URL = f'https://www.mashina.kg/motosearch/all/?page={i}'

    response = requests.get(URL)

    soup = BS(response.text, 'html.parser')

    cards = soup.find_all('div', {'class': 'list-item'})

    list_ = []
    for card in cards:
        title = card.find('h2', {'class': 'name'}).text.strip()
        
        price = card.find('p', {'class': 'price'}).text.replace('  ', '').replace('\n', '').strip()

        link = (card.find('img').get('data-src'))
        if card.find("p", {"class": "year-miles"}).text :
            description_year = card.find("p", {"class": "year-miles"}).text.replace("\n", "").replace('  ', '')
        else:
            description_year = 'Год не указана'
        if card.find("p", {"class": "body-type"}).text:
            description_body = card.find("p", {"class": "body-type"}).text.replace("\n", "").replace('  ', '')
        else:
            description_body = 'Нет названия'
        if card.find("p", {"class": "volume"}):
            description_volume =  card.find("p", {"class": "volume"}).text.replace("\n", "").replace('  ', '')
        else:
            description_volume = 'Нет пробега'
        total_description = f'{description_body} {description_volume} {description_year}'


        list_.append([title, price, link, total_description])

    with open('mashina.csv', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(list_)


