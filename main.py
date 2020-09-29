import requests
from pprint import pprint

# Hard code request
# response = requests.get('https://api.telegram.org/bot187988593:AAH2bUUIAgGDvlnXlNshjD6cNoGVg4qGZLE/getMe')

# print(response.text)

# More clean code

TOKEN = '1324065101:AAF23TNO8EXW_JT6bdXo7bDOxfa3agGvJNI'


url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url=url)

pprint(response.json())
