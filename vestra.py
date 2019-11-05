import telebot
from telebot import apihelper, types
import config
import geopy


apihelper.proxy = {'https':config.SOCKS_PROXY}


bot = telebot.TeleBot(config.TOKEN)
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup_adress = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup_school = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup_tip_zan = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup_instruktor = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

btn_raspisanie = types.KeyboardButton('Расписание школы')
btn_adress = types.KeyboardButton('Адреса проведения занятий', request_location=True)
btn_studeniy = types.KeyboardButton('Лекции на Студеном')
btn_aviamotornaya = types.KeyboardButton('Лекции на Авиамоторной')
btn_polushkino = types.KeyboardButton('Тренировки в Полушкино')
btn_NU = types.KeyboardButton('Я ученик НУ')
btn_BU = types.KeyboardButton('Я ученик БУ')
btn_SU = types.KeyboardButton('Я ученик СУ')
btn_obshie = types.KeyboardButton('Общешкольные занятия')
btn_instruktor = types.KeyboardButton('Инструктор')
btn_Ivanov = types.KeyboardButton('Иванов')
btn_Petrov = types.KeyboardButton('Петров')
btn_Matusko = types.KeyboardButton('Матуско')

markup_menu.add(btn_raspisanie, btn_adress)
markup_adress.add(btn_studeniy, btn_aviamotornaya, btn_polushkino)
markup_school.add(btn_NU, btn_BU, btn_SU)
markup_tip_zan.add(btn_obshie, btn_instruktor)
markup_instruktor.add(btn_Ivanov, btn_Petrov, btn_Matusko)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, вестровец!', reply_markup=markup_menu)

@bot.message_handler(func=lambda message: True, content_types=['location'])
def uroki_location(message):
    lon = message.location.longitude
    lat = message.location.latitude
    if message.text == 'Лекции на Студеном':
        bot.send_venue(message.chat.id,
                       config.LOCAT[1]['title'],
                       config.LOCAT[1]['latm'],
                       config.LOCAT[1]['lonm'],
                       config.LOCAT[1]['adress']
                       )
    elif message.text == 'Лекции на Авиамоторной':
        bot.send_venue(message.chat.id,
                       config.LOCAT[2]['title'],
                       config.LOCAT[2]['latm'],
                       config.LOCAT[2]['lonm'],
                       config.LOCAT[2]['adress']
                       )
    elif message.text == 'Тренировки в Полушкино':
        bot.send_venue(message.chat.id,
                       config.LOCAT[0]['title'],
                       config.LOCAT[0]['latm'],
                       config.LOCAT[0]['lonm'],
                       config.LOCAT[0]['adress']
                       )

@bot.message_handler(func=lambda message: True)
def echo_1(message):
    if message.text == 'Расписание школы':
        bot.reply_to(message, 'Где учишься?',  reply_markup=markup_school)
    elif message.text == 'Адреса проведения занятий':
        bot.reply_to(message, 'Выбери место', reply_markup=markup_adress)
        uroki_location(message)
    else:
        bot.reply_to(message, message.text, reply_markup=markup_menu)


bot.polling()