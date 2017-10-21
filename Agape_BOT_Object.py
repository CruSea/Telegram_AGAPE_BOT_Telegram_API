import telebot
from telebot import types
import json
class Agape_BOT_Object:
    def __init__(self):
        pass

    def generate_keyboard_markup(self, json_array_object, row_width):
        menus = json_array_object
        if(menus['Sub_Menus']):
            keyboard_markup = types.ReplyKeyboardMarkup(row_width=row_width)
            for menu in menus['Sub_Menus']:
                keyboard_markup.add(self._get_single_menu(menu))
            print keyboard_markup
            return keyboard_markup

    def _get_single_menu(self, json_object):
        menu_item = types.KeyboardButton(json_object['Replay']['Name'])
        return menu_item
