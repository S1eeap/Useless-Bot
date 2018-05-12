#506785758:AAHCPrm5smYcV2zGqU4PEGDhson55n_nkcc
import requests
from time import sleep
import os
url = "https://api.telegram.org/bot506785758:AAHCPrm5smYcV2zGqU4PEGDhson55n_nkcc/"


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def get_message(update):
    message = update['message']['text']
    return message

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main():
    text_out = ""
    update_id = last_update(get_updates_json(url))['update_id']
    update = last_update(get_updates_json(url))
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            text_in = update['message']['text']
            first_name = update['message']['from']['first_name']
            last_name = update['message']['from']['last_name']
            #print(first_name, last_name, ':', text_in)
            send_mess(get_chat_id(last_update(get_updates_json(url))), text_in)
            update_id += 1
        sleep(1)

if __name__ == '__main__':
    main()
