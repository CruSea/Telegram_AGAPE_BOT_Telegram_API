import requests
class Agape_Http:
    def __init__(self, bot_token):
        self.Main_URL = "http://localhost:8000"
        self.BOT_TOKEN = bot_token;
        pass

    def send_post_request(self):
        r = requests.post(self.Main_URL, data={'number': 12524, 'type': 'issue', 'action': 'show'})
        return r

    def request_menu(self, menu_id):
        response = requests.post(self.Main_URL, data={'bot_token': self.BOT_TOKEN, 'menu_id': menu_id})

    def request_starter_menu(self):
        response = requests.post(self.Main_URL, data={'bot_token': self.BOT_TOKEN, 'menu_id': 'get_start'})
        return response.json()
    def request_sub_menu(self, menu_id):
        response = requests.post(self.Main_URL, data={'bot_token': self.BOT_TOKEN, 'menu_id': menu_id})
        return response.json()