import telebot
import os

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start')
    user_markup.row('Ассортимент')
    user_markup.row('Акции')
    user_markup.row('Отзывы и предложения')
    user_markup.row('"Возврат и гарантии')
    bot.send_message(message.from_user.id, 'Добро пожаловать! Я бот компании, приятно познакомиться!',
                     reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!!!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


bot.polling(none_stop=True)
