import requests
from pprint import pprint

# Hard code request
# response = requests.get('https://api.telegram.org/bot187988593:AAH2bUUIAgGDvlnXlNshjD6cNoGVg4qGZLE/getMe')

# print(response.text)

# More clean code


def sendMessage(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    parameter = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.get(url=url, params=parameter)


TOKEN = '1324065101:AAF23TNO8EXW_JT6bdXo7bDOxfa3agGvJNI'


# url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

# response = requests.get(url=url)

# data = response.json()['result'][0]
# message = data['message']
# chat = data['message']['chat']
# from1 = data['message']['from']
# text = data['message']['text']
# pprint(text)
i = 0
while True:
    chat_id = 86775091
    i += 1
    sendMessage(chat_id, f'Salom:{i}')
