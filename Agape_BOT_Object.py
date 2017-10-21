import telebot
from telebot import types
import json
class Agape_BOT_Object:
    def __init__(self):
        pass

    def generate_keyboard_markup(self, json_array_object, row_width):
        menus = json.loads(json_array_object)
        keyboard_markup = types.ReplyKeyboardMarkup(row_width=row_width)
        for menu in menus:
            keyboard_markup.add(self._get_single_menu(menu))
        return keyboard_markup

    def _get_single_menu(self, json_object):
        menu_item = types.KeyboardButton(json_object['name'])
        return menu_item
