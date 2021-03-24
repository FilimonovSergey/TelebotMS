import telebot

bot = telebot.TeleBot('1704279792:AAHEN-zVs0yEAA2ImGc7PLTOQA7A7yIfCEI')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Я бот. Приятно познакомиться')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


bot.polling(none_stop=True)
