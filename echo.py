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
    update_id = []
    # update_id = update['result'][-1]['update_id']
    for i in data:
        chat_id.append(i['message']['chat']['id'])
        # update_id.append(i[])

    # message = data['message']
    # chat = data['message']['chat']
    # from1 = data['message']['from']
    # text = data['message']['text']
    # chat_id = chat['id']
    return chat_id


TOKEN = '187988593:AAH2bUUIAgGDvlnXlNshjD6cNoGVg4qGZLE'


# pprint(text)
# sendMessage
i = 0
while True:
    chat_id = getUpdates()
    i += 1
    for idx in chat_id:
        sendMessage(idx, f'Salom:{i}')
