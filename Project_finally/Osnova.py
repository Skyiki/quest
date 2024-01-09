import telebot
import json

token = "6844377304:AAH_4C06uPoCM46jZZp7UVauwBVBY9hDSF8"



user = {}

with open('player.json', 'w+') as file:
    json.dump(user, file)