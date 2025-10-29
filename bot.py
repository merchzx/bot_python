# 1
# python.exe -m pip install --upgrade pip
# or
# pip install --upgrade pip
import datetime
# 2
# python.exe -m pip install -r requirements.txt
# or
# pip install -r requirements.txt



import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("TOKEN")

url = f"https://api.telegram.org/bot{bot_token}/"  # don't forget to change the token!


def last_update(request):
    response = requests.get(request + 'getUpdates')
    print(response)
    response = response.json()
    print(response)
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update['message']['text']
    return message_text


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(url)['update_id']
    while True:
        # pythonanywhere
        update = last_update(url)
        if update_id == update['update_id']:
            if get_message_text(update).lower() == 'hi' or get_message_text(
                    update).lower() == 'hello' or get_message_text(update).lower() == 'hey':
                send_message(get_chat_id(update), 'Greetings! Type "Dice" to roll the dice!')
            elif get_message_text(update).lower() == 'qa24':
                send_message(get_chat_id(update), 'Python')
            elif get_message_text(update).lower() == 'python':
                send_message(get_chat_id(update), 'version 3.10')
            elif get_message_text(update).lower() == 'dice':
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                send_message(get_chat_id(update),
                             'You have ' + str(_1) + ' and ' + str(_2) + '!\nYour result is ' + str(_1 + _2) + '!')
            elif get_message_text(update).lower() == 'who':
                send_message(get_chat_id(update),
                             "I dont know who are u??"
                             )
            elif get_message_text(update).lower() == 'show':
                send_message(get_chat_id(update),
                             f"What do u want me to show?"
                             )
            elif get_message_text(update).lower() == 'time':
                send_message(get_chat_id(update),
                             f"{datetime.time}"
                             )
            else:
                send_message(get_chat_id(update), 'Sorry, I don\'t understand you :(')
            update_id += 1


# print(__name__)
if __name__ == '__main__':
    main()
# print(__name__)
# print('HELLO') #При подключении файла как бибилиотеки import bot, в другой .py файл проекта, этот код будет запускатся при включении того, другого файла
