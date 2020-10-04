import requests
from pprint import pprint

# Hard code request
# response = requests.get('https://api.telegram.org/bot187988593:AAH2bUUIAgGDvlnXlNshjD6cNoGVg4qGZLE/getMe')

# print(response.text)

# @tutorial_1bot
TOKEN = '1324065101:AAF23TNO8EXW_JT6bdXo7bDOxfa3agGvJNI'


def sendMessage(id, txt):
    k = {
        'text': '1'
    }

    keyboard = [
        [k, k],
        [k, k]
    ]
    replyKeyboardMarkup = {
        'keyboard': keyboard
    }

    parameter = {
        'chat_id': id,
        'text': txt,
        'reply_markup': replyKeyboardMarkup,
    }

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    response = requests.get(url=url, json=parameter)


sendMessage('86775091', 'TXT')
