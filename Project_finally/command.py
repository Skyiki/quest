import telebot
import Osnova
import json
from telebot import types

bot = telebot.TeleBot(token=Osnova.token)

@bot.message_handler(commands=['start'])
def start_func(message):
    keyboard = types.InlineKeyboardMarkup()
    #создание и добавление кнопок на созданную клавиатуру
    button1 = types.InlineKeyboardButton(text='Да!', callback_data='button1')
    button2 = types.InlineKeyboardButton(text='Нет', callback_data='button2')
    keyboard.add(button1)
    keyboard.add(button2)

    #отправление пользователю сообщения
    bot.send_message(message.chat.id, "Вы находитесь на онлайн квесте. Вы готовы начать?", reply_markup=keyboard)

#Функция запустится, когда пользователь нажмет на кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_Inline(call):
    if call.message:
        if call.data == "button1":
            keyboard = types.InlineKeyboardMarkup()
            but1 = types.InlineKeyboardButton(text='Закричать', callback_data='but1')
            but2 = types.InlineKeyboardButton(text='Смириться', callback_data='but2')
            but3 = types.InlineKeyboardButton(text='Попытаться двигаться', callback_data='3')
            keyboard.add(but1, but2, but3)

            bot.send_message(call.message.chat.id, 'Вы чувствуете, что под вами нет твердой поверхности.'
                                                   'Вы открываете глаза, пытаясь понять, что происходит.'
                                                   ' Как только вы открываете глаза, то вас охватывает страх.'
                                                   'Вы падаете. Вы пытаетесь успокоиться и к счастью вам это удается.'
                                                   ' Вы решаете:', reply_markup=keyboard)

        if call.data == "button2":
            bot.send_message(call.message.chat.id, 'Хорошо. Если передумаете, то нажмите /start')
#потом бот должен спросить как обращаться к пользователю
bot.polling()