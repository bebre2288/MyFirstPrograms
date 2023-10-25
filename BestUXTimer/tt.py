import telebot;
bot = telebot.TeleBot('1274090617:AAHfk5nAOgy3vATlPfnqD3K-H2_0d1udCII');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "введите время")
        
    elif message.text == "таймер":
        bot.send_message(message.from_user.id, "Время")
        age = int(message.text)
    else:
        bot.send_message(message.from_user.id, "idi v zhopy")
bot.polling(none_stop=True, interval=0)
