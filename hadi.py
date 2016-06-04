import telebot
from telebot import types

TOKEN = '239519305:AAH-1nJiWwqyigWQvg-qxZKpo6nnKpGh2sU' #Ponemos nuestro TOKEN generado con el @BotFather
bot = telebot.TeleBot(TOKEN)


markup = types.ReplyKeyboardMarkup()
markup.row('a')
markup.row('b')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi, how you doing?", reply_markup=markup)

@bot.message_handler(regexp="stressed")
def handle_message(message):
    # pass
    bot.reply_to(message, "Oooh, sorry to hear it. What is stressing you??")

@bot.message_handler(regexp="boring")
def handle_message_(message):
    # pass
    bot.reply_to(message, "Do you want to do something?")



bot.polling()
