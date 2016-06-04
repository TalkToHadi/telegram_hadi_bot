import telebot
from state_machine import *

TOKEN = '239519305:AAH-1nJiWwqyigWQvg-qxZKpo6nnKpGh2sU' #Ponemos nuestro TOKEN generado con el @BotFather
bot = telebot.TeleBot(TOKEN)


currentState = Initial()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(answer):
    bot.send_message(
        answer.chat.id,
        currentState.message,
        reply_markup=currentState.markup())

@bot.message_handler(func=lambda m: True)
def handle_message(answer):
    chat_id = answer.chat.id
    currentState = currentState.next(answer.text)
    bot.send_message(
        chat_id,
        currentState.message,
        reply_markup=currentState.markup())


bot.polling()
