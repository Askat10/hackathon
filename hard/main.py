import requests
from bs4 import BeautifulSoup as BS
import telebot
from decouple import config
from telebot import types
import datetime


TOKEN = config('TOKEN')
BOT = telebot.TeleBot(TOKEN)
kbord = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
go = types.KeyboardButton('Начать')
finish = types.KeyboardButton('Остановить')
kbord.add(go, finish)
now = datetime.datetime.now()
datestring = now.strftime("%Y-%m-%d")
@BOT.message_handler(commands=['start'])
def start(message):
    BOT.send_message(message.chat.id, f'Здарова {message.from_user.first_name}! Я покажу тебе сегодняшние новости! А источником самих новостей будет Kaktus Media. Газету дать?')
    BOT.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIiWtkNQABbvM4Gx5_97kaBSumYWZDLb0AAisAA5V7sgpxuD9N59llsi8E')
    BOT.send_message(message.chat.id,'выа', reply_markup=kbord)
    


@BOT.message_handler(content_types=['text'])
def any(message):
    if (message.text == 'Начать'):
        markup = types.InlineKeyboardMarkup(row_width=5)
        k1 = types.InlineKeyboardButton(1, callback_data='1')
        k2 = types.InlineKeyboardButton(2, callback_data='2')
        k3 = types.InlineKeyboardButton(3, callback_data='3')
        k4 = types.InlineKeyboardButton(4, callback_data='4')
        k5 = types.InlineKeyboardButton(5, callback_data='5')
        k6 = types.InlineKeyboardButton(6, callback_data='6')
        k7 = types.InlineKeyboardButton(7, callback_data='7')
        k8 = types.InlineKeyboardButton(8, callback_data='8')
        k9 = types.InlineKeyboardButton(9, callback_data='9')
        k10 = types.InlineKeyboardButton(10, callback_data='10')
        k11 = types.InlineKeyboardButton(11, callback_data='11')
        k12 = types.InlineKeyboardButton(12, callback_data='12')
        k13 = types.InlineKeyboardButton(13, callback_data='13')
        k14 = types.InlineKeyboardButton(14, callback_data='14')
        k15 = types.InlineKeyboardButton(15, callback_data='15')
        k16 = types.InlineKeyboardButton(16, callback_data='16') 
        k17 = types.InlineKeyboardButton(17, callback_data='17')
        k18 = types.InlineKeyboardButton(18, callback_data='18')
        k19 = types.InlineKeyboardButton(19, callback_data='19')
        k20 = types.InlineKeyboardButton(20, callback_data='20')
        markup.add(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20)
        BOT.send_message(message.chat.id, parsing(message.text))
        BOT.send_sticker(message.chat.id,'CAACAgIAAxkBAAEIiX5kNQABwxbb56VPxJoh1oUXyMZzyMYAAjIAA5V7sgrf7pNeBb9WYS8E')
        BOT.send_message(message.chat.id, 'Выбери номер новости', reply_markup=markup)
    elif(message.text == 'Остановить'):
        BOT.send_message(message.chat.id, 'Чао!')
        BOT.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIjXhkNo73USTUw4kFZLdxmre-CiD6wwACLQADlXuyCvLhEuI_S6j3LwQ')

@BOT.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        URL = f'https://kaktus.media/?lable=8&date=a{datestring}&order=time'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0, win64; x64) AppleWebKit/537.36 (KHTML., like Gecko) Chrome/68.0.3029.10 Safari/537.3'}
        response = requests.get(URL, headers=headers)
        soup = BS(response.content, 'html.parser')
        cards = soup.find_all('div', {'class': 'ArticleItem'})
        new_url = cards[int(call.data)-1].find('a').get('href')

        response2 = requests.get(new_url, headers=headers)
        soup2 = BS(response2.content, 'html.parser')
        messes = soup2.find_all('p')
        string = ''
        for mess in messes:
            nmess = mess.text
            string += nmess
    
        BOT.send_message(call.message.chat.id, string)

def parsing(message):
    URL = f'https://kaktus.media/?lable=8&date={datestring}&order=time'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0, win64; x64) AppleWebKit/537.36 (KHTML., like Gecko) Chrome/68.0.3029.10 Safari/537.3'}
    response = requests.get(URL, headers=headers)
    soup = BS(response.content, 'html.parser')
    cards = soup.find_all('div', {'class': 'ArticleItem'})
    list_ = []
    for card in cards:
        res = card.find('a', {'class': 'ArticleItem--name'}).text.strip()
        list_.append(f'{cards.index(card)+1}. {res}\n')
    list_ = list_[:20]
    string = ''.join(list_)
    return string





BOT.polling(none_stop=True, interval=0)