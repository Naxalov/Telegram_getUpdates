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


def getUpdates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

    response = requests.get(url=url)

    data = response.json()['result']
    chat_id = []
    for i in data:
        chat_id.append(i['message']['chat']['id'])

    # message = data['message']
    # chat = data['message']['chat']
    # from1 = data['message']['from']
    # text = data['message']['text']
    # chat_id = chat['id']
    return chat_id


TOKEN = '1324065101:AAF23TNO8EXW_JT6bdXo7bDOxfa3agGvJNI'


# pprint(text)
i = 0
while True:
    chat_id = getUpdates()
    i += 1
    for idx in chat_id:
        sendMessage(idx, f'Salom:{i}')
