import Agape_BOT_Object
import telebot
import Agape_Http
from telebot import types
import json

AgapeHttp = Agape_Http.Agape_Http("1")
print AgapeHttp.request_starter_menu().json()