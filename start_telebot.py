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
    user_markup.row('Доставка и оплата')
    bot.send_message(message.from_user.id, 'Добро пожаловать! Я бот компании, приятно познакомиться!',
                     reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!!!')
    elif message.text == 'Ассортимент':
        bot.send_message(message.from_user.id,
                         'Вы можете ознакомиться с нашим ассортиментом, перейдя по следующей ссылке:'
                         'https://melodiasna.ru/')
    elif message.text == 'Акции':
        bot.send_message(message.from_user.id,
                         'Вы можете ознакомиться с действующими акциями, перейдя по следующей ссылке:'
                         'https://melodiasna.ru/actions/')
    elif message.text == 'Отзывы и предложения':
        bot.send_message(message.from_user.id,
                         'Для того, чтобы ознакомиться с отзывами о продуктах нашей компании, '
                         'а также оставить свой  отзыв или предложение, перейдите по следующей ссылке:'
                         'https://melodiasna.ru/o-produkte/reviews/')
    elif message.text == 'Доставка и оплата':
        bot.send_message(message.from_user.id,
                         'Для того, чтобы ознакомиться с информацией о доставке и оплате товаров,'
                         'перейдите по следующей ссылке:'
                         'https://melodiasna.ru/dostavka-i-oplata/')
    else:
        bot.send_message(message.from_user.id, 'Будем рады видеть Вас в наших фирменных магазинах')


bot.polling(none_stop=True)
