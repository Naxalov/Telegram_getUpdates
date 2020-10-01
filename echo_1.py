import requests
from pprint import pprint

# Hard code request
# response = requests.get('https://api.telegram.org/bot187988593:AAH2bUUIAgGDvlnXlNshjD6cNoGVg4qGZLE/getMe')

# print(response.text)

# @tutorial_1bot
TOKEN = '1324065101:AAF23TNO8EXW_JT6bdXo7bDOxfa3agGvJNI'


def getUpdates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url=url)
    if response.status_code:
        update = response.json()

    return update


def get_message(update):
    txt = update['result'][-1]['message']['text']
    update_id = update['result'][-1]['update_id']
    return txt, update_id


def sendMessage(id, txt):

    parameter = {
        'chat_id': id,
        'text': txt,
        'disable_notification': True,
    }

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    response = requests.get(url=url, params=parameter)


last_update_id = -5
while True:
    x = getUpdates()
    txt, update_id = get_message(x)
    print(f'update_id: {update_id} last_id:{last_update_id}')
    if last_update_id != update_id:
        sendMessage(86775091, txt+'\U0001F601')
        last_update_id = update_id
