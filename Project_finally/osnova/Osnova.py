import telebot
import json

token = ''

bot = telebot.TeleBot(token=token)

user = {}

with open('player.json', 'w+') as file:
    json.dump(user, file)

@bot.message_handler(content_types=["video"])
def video_func(message):
    bot.reply_to(message.chat.id, text="Этот контент не поддерживается ботом. \n"
                               "Нажмите /start для перезапуска"
                 )


@bot.message_handler(content_types=["photo"])
def photo_func(message):
    bot.reply_to(message.chat.id, text="Этот контент не поддерживается ботом. \n"
                               "Нажмите /start для перезапуска"
                 )


@bot.message_handler(content_types=["animation"])
def animation_func(message):
    bot.reply_to(message.chat.id, text="Этот контент не поддерживается ботом. \n"
                               "Нажмите /start для перезапуска"
                 )


@bot.message_handler(content_types=["audio"])
def audio_func(message):
    bot.reply_to(message.chat.id, text="Этот контент не поддерживается ботом. \n"
                               "Нажмите /start для перезапуска"
                 )


@bot.message_handler(content_types=["sticker"])
def sticker_func(message):
    bot.reply_to(message.chat.id, text="Этот контент не поддерживается ботом. \n"
                               "Нажмите /start для перезапуска"
                 )

@bot.message_handler(content_types=["text"])
def text_func(message):
    bot.reply_to(message.chat.id, text="Этот контент не поддерживается ботом. \n"
                               "Нажмите /start для перезапуска"
                 )
