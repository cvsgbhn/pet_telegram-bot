import telebot

bot = telebot.TeleBot('token')

##apihelper.proxy = {'https':'socks5://userproxy:password@proxy_address:port'}

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text in "Код для подтверждения номера телефона:":
        bot.send.message(message.from_user.id, "Вижу код")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)
