import telebot
import os
import sqlite3

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start')
    user_markup.row('Все маршруты')
    user_markup.row('Пройденные маршруты')
    user_markup.row('Не пройденные маршруты')
    user_markup.row('Добавить маршрут')
    bot.send_message(message.from_user.id, 'Вечер в хату! Чем помочь, бродяга?',
                     reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Здарова! Как жизнь?')
    elif message.text == 'Все маршруты':
        all_routes(message)
    elif message.text == 'Пройденные маршруты':
        check_routes()
    elif message.text == 'Не пройденные маршруты':
        no_check_routes()
    elif message.text == 'Добавить маршрут':
        add_route(message)
    else:
        bot.send_message(message.from_user.id, 'Заходи ещё!')


def all_routes(message):
    conn = sqlite3.connect('routes.db')
    cur = conn.cursor()
    cur.execute("SELECT * from routes")
    table_all_routes = cur.fetchall()
    bot.send_message(message.from_user.id, table_all_routes)


def check_routes():
    None


def no_check_routes():
    None


def add_route(message):
    conn = sqlite3.connect('routes.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routes VALUES(?, ?, ?, ?);")
    conn.commit()
    bot.send_message(message.from_user.id, 'Твой маршрут добавлен')


bot.polling(none_stop=True)
