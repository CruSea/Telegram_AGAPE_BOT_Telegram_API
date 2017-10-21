import Agape_BOT_Object
import telebot
from telebot import types

bot = telebot.TeleBot("208413095:AAFflQth4lhFdXUQkJaHjemOfIqFRZT2_DU")
agape_object = Agape_BOT_Object.Agape_BOT_Object()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "hi", reply_markup=agape_object.generate_keyboard_markup('[{"name":"Menu1"},{"name":"Menu2"},{"name":"Menu3"}]',2))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print message
    replay_send(message)

def replay_send(message):
    if(message.text == 'help'):
        bot.send_message(message.chat.id, "A", reply_markup=menu1)

bot.polling()