import Agape_BOT_Object
import telebot
import Agape_Http
from telebot import types

bot = telebot.TeleBot("208413095:AAFflQth4lhFdXUQkJaHjemOfIqFRZT2_DU")
agape_object = Agape_BOT_Object.Agape_BOT_Object()
AgapeHttp = Agape_Http.Agape_Http("AAFflQth4lhFdXUQkJaHjemOfIqFRZT2_DU")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    response = AgapeHttp.request_starter_menu()
    bot.send_message(message.chat.id, response['Description'], reply_markup=agape_object.generate_keyboard_markup(response, 2))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    replay_send(message)

def replay_send(message):
    if(message.text == 'help' or message.text == 'start'):
        pass
    else:
        response = AgapeHttp.request_sub_menu("Content2")
        bot.send_message(message.chat.id, "A", reply_markup=agape_object.generate_keyboard_markup(response, 2))
bot.polling()