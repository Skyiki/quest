import telebot
from Project_finally.osnova import Osnova
import json
from telebot import types

bot = telebot.TeleBot(token=Osnova.token)

try:
    with open('osnova/player.json', 'r') as file:
        players = json.load(file)
except:
    players = {}

with open('text_for_quest/text.json', 'r') as file:
    text = json.load(file)


@bot.message_handler(commands=['start'])
def start_func(message):
    user_id = message.chat.id

    keyboard = types.InlineKeyboardMarkup()
    # создание и добавление кнопок на созданную клавиатуру
    button1 = types.InlineKeyboardButton(text='Да!', callback_data='button1')
    button2 = types.InlineKeyboardButton(text='Нет', callback_data='button2')
    keyboard.add(button1)
    keyboard.add(button2)
    bot.send_message(message.chat.id, "Вы находитесь на онлайн квесте. Вы готовы начать?", reply_markup=keyboard)
    # отправление пользователю сообщения

# Функция запустится, когда пользователь нажмёт на кнопку
@bot.callback_query_handler(func=lambda call: call.data == "button1")# локация start, lvl 1
def callback_Inline(call):
    user_id = call.message.chat.id

    if user_id in players:
        keyboard = types.InlineKeyboardMarkup()
        # создание и добавление кнопок на созданную клавиатуру
        button1 = types.InlineKeyboardButton(text='Да!', callback_data='yes')
        button2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(button1)
        keyboard.add(button2)
        bot.send_message(call.message.chat.id, "Внимание! Найдена незаконченная игра. Хотите продолжить?",
                         reply_markup=keyboard)

    elif user_id not in players:
        players[user_id] = {}
        players[user_id]['location'] = 'start'
        players[user_id]['lvl'] = "1"

        with open('osnova/player.json', 'w+') as file:
            json.dump(players, file)

        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton(text='Закричать', callback_data='butonss1')
        but2 = types.InlineKeyboardButton(text='Смириться', callback_data='butonss2')
        but3 = types.InlineKeyboardButton(text='Попытаться двигаться', callback_data='butonss3')
        keyboard.add(but1)
        keyboard.add(but2)
        keyboard.add(but3)

        bot.send_photo(call.message.chat.id, open("photo/kandinsky-download-1705160908366.png", "rb"),
                       caption= text['start'], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def yes_func(call):
    user_id = call.message.chat.id
    if players[user_id]['location'] == 'start' and players[user_id]['lvl'] == "1":
        players[user_id] = {}
        players[user_id]['location'] = 'start'
        players[user_id]['lvl'] = "1"

        with open('osnova/player.json', 'w+') as file:
            json.dump(players, file)

        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton(text='Закричать', callback_data='but1')
        but2 = types.InlineKeyboardButton(text='Смириться', callback_data='but2')
        but3 = types.InlineKeyboardButton(text='Попытаться двигаться', callback_data='but3')
        keyboard.add(but1)
        keyboard.add(but2)
        keyboard.add(but3)

        bot.send_photo(call.message.chat.id, open("photo/kandinsky-download-1705160908366.png", "rb"),
                       caption=text['start'], reply_markup=keyboard)

    elif players[user_id]['location'] == 'cat' and players[user_id]['lvl'] == "2":
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Погладить', callback_data='butt1')
        but2 = types.InlineKeyboardButton('Взять кота на руки', callback_data='butt2')
        but3 = types.InlineKeyboardButton('Отойти подальше', callback_data='butt3')
        keyboard.row(but1)
        keyboard.add(but2)
        keyboard.add(but3)

        bot.send_photo(call.message.chat.id, open('photo/Cat.png', 'rb'), caption=text['cat'], reply_markup=keyboard)

    elif players[user_id]['location'] == 'cat1' and players[user_id]['lvl'] == "3":
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Тут нельзя оставаться. Пойти искать выход', callback_data='buut1')
        but2 = types.InlineKeyboardButton('Кот такой милый останусь с ним.', callback_data='buut2')
        keyboard.row(but1)
        keyboard.add(but2)

        bot.send_photo(call.message.chat.id, open('photo/Cat1.png', 'rb'), caption=text['cat1 lvl3'], reply_markup=keyboard)

    elif players[user_id]['location'] == 'cat3' and players[user_id]['lvl'] == "3":
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Побежать в случайную сторону', callback_data='buuut1')
        but2 = types.InlineKeyboardButton('Остаться на месте', callback_data='buuut2')
        keyboard.row(but1)
        keyboard.add(but2)

        bot.send_photo(call.message.chat.id, open("photo/cat3_lvl3.png", 'rb'), caption=text['cat3 lvl3'],
                       reply_markup=keyboard)

    elif players[user_id]['location'] == 'tokyo' and players[user_id]['lvl'] == "2":
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Заговорить с людьми', callback_data='buttt1')
        but2 = types.InlineKeyboardButton('Всё как-нибудь само решится', callback_data='buttt2')
        but3 = types.InlineKeyboardButton('Взять случайного прохожего за руку', callback_data='buttt3')
        keyboard.row(but1)
        keyboard.add(but2)
        keyboard.add(but3)

        bot.send_photo(call.message.chat.id, open('photo/Tokyo.png', 'rb'), caption=text['tokyo'], reply_markup=keyboard)

    elif players[user_id]['location'] == 'tokyo1' and players[user_id]['lvl'] == "3":
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('*сказать правду*', callback_data='buton1')
        but2 = types.InlineKeyboardButton('*сказать, что вы потеряли память*', callback_data='buton2')
        but3 = types.InlineKeyboardButton('*сказать что-то другое*', callback_data='buton3')
        keyboard.row(but1)
        keyboard.add(but2)
        keyboard.add(but3)

        bot.send_photo(call.message.chat.id, open('photo/tokyo1_lvl3.jpg', 'rb'), caption=text['tokyo1 lvl3'],
                       reply_markup=keyboard)

    elif players[user_id]['location'] == 'tokyo3' and players[user_id]['lvl'] == "3":
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('*солгать ему*', callback_data='butot1')
        but2 = types.InlineKeyboardButton('*сказать правду*', callback_data='butot2')
        but3 = types.InlineKeyboardButton('*извиниться за то, что побеспокоили его*', callback_data='butot3')
        keyboard.row(but1)
        keyboard.add(but2)
        keyboard.add(but3)

        bot.send_photo(call.message.chat.id, open('photo/tokyo3_lvl3.jpg', 'rb'), caption=text['tokyo3 lvl3'],
                       reply_markup=keyboard)

    elif players[user_id]['location'] == '3 hero' and players[user_id]['lvl'] == "2":
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Пойти вперёд', callback_data='butttt1')
        but2 = types.InlineKeyboardButton('Остаться на месте', callback_data='butttt2')
        keyboard.row(but1)
        keyboard.add(but2)

        bot.send_photo(call.message.chat.id, open('photo/3_hero.png', 'rb'), caption=text['3hero lvl2'],
                       reply_markup=keyboard)

    elif players[user_id]['location'] == '3 hero1' and players[user_id]['lvl'] == "3":
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton("Пройти в крепость", callback_data='buttons1')
        but2 = types.InlineKeyboardButton('Остаться на опушке леса', callback_data='buttons2')
        but3 = types.InlineKeyboardButton('Пойти дальше исследовать мир', callback_data='')
        keyboard.add(but1)
        keyboard.add(but2)
        keyboard.add(but3)

        bot.send_photo(call.message.chat.id, open("photo/3_hero2.png", 'rb'), caption=text['3hero1 lvl3'],
                       reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "no")
def no_func(call):
    user_id = call.message.chat.id
    players[user_id] = {}
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(text='Закричать', callback_data='butonss1')
    but2 = types.InlineKeyboardButton(text='Смириться', callback_data='butonss2')
    but3 = types.InlineKeyboardButton(text='Попытаться двигаться', callback_data='butonss3')
    keyboard.add(but1)
    keyboard.add(but2)
    keyboard.add(but3)

    bot.send_photo(call.message.chat.id, open("photo/kandinsky-download-1705160908366.png", "rb"),
                   caption=text['start'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "button2")
def callback_Inlinee(call):
    bot.send_message(call.message.chat.id, 'Хорошо. Если передумаете, то нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'butonss1')# локация cat, lvl 2
def butonss1(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'cat'
    players[user_id]['lvl'] = "2"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Погладить', callback_data='butt1')
    but2 = types.InlineKeyboardButton('Взять кота на руки', callback_data='butt2')
    but3 = types.InlineKeyboardButton('Отойти подальше', callback_data='butt3')
    keyboard.row(but1)
    keyboard.add(but2)
    keyboard.add(but3)

    bot.send_photo(call.message.chat.id, open('photo/Cat.png', 'rb'), caption=text['cat'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "butt1")# локация cat1, lvl 3
def butt1(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'cat1'
    players[user_id]['lvl'] = "3"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Тут нельзя оставаться. Пойти искать выход', callback_data='buut1')
    but2 = types.InlineKeyboardButton('Кот такой милый останусь с ним.', callback_data='buut2')
    keyboard.row(but1)
    keyboard.add(but2)

    bot.send_photo(call.message.chat.id, open('photo/Cat1.png', 'rb'), caption=text['cat1 lvl3'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "buut1")# локация cat1, lvl 4
def buut1(call):
    user_id = call.message.chat.id
    bot.send_photo(call.message.chat.id, open('photo/cat1_lvl4.png', 'rb'), caption=text['cat1 lvl4'])

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == "buut2")# локация cat2, lvl 4
def buut2(call):
    user_id = call.message.chat.id
    bot.send_photo(call.message.chat.id, open('photo/cat1_lvl5.png', 'rb'), caption=text['cat2 lvl4'])

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == "butt2")# локация cat2, lvl 3
def butt2(call):
    user_id = call.message.chat.id
    bot.send_message(call.message.chat.id, text=text['cat2 lvl3'])

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == "butt3")# локация cat3, lvl 3
def butt3(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'cat3'
    players[user_id]['lvl'] = "3"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Побежать в случайную сторону', callback_data='buuut1')
    but2 = types.InlineKeyboardButton('Остаться на месте', callback_data='buuut2')
    keyboard.row(but1)
    keyboard.add(but2)

    bot.send_photo(call.message.chat.id, open("photo/cat3_lvl3.png", 'rb'), caption=text['cat3 lvl3'], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "buuut1")# локация cat1, lvl 5
def buuut1(call):
    user_id = call.message.chat.id

    bot.send_photo(call.message.chat.id, open('photo/cat1_lvl5.png', 'rb'), caption=text['cat1 lvl5'])

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)


@bot.callback_query_handler(func=lambda call: call.data == "buuut2")# локация cat2, lvl 5
def buuut2(call):
    user_id = call.message.chat.id

    bot.send_photo(call.message.chat.id, open('photo/cat2_lvl5.png', 'rb'), caption=text['cat2 lvl5'])

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'butonss2')# локация tokyo, lvl 2
def butonss2(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'tokyo'
    players[user_id]['lvl'] = "2"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Заговорить с людьми', callback_data='buttt1')
    but2 = types.InlineKeyboardButton('Всё как-нибудь само решится', callback_data='buttt2')
    but3 = types.InlineKeyboardButton('Взять случайного прохожего за руку', callback_data='buttt3')
    keyboard.row(but1)
    keyboard.add(but2)
    keyboard.add(but3)

    bot.send_photo(call.message.chat.id, open('photo/Tokyo.png', 'rb'), caption=text['tokyo'], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'buttt1')# локация tokyo1, lvl 3
def buttt1(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'tokyo1'
    players[user_id]['lvl'] = "3"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('*сказать правду*', callback_data='buton1')
    but2 = types.InlineKeyboardButton('*сказать, что вы потеряли память*', callback_data='buton2')
    but3 = types.InlineKeyboardButton('*сказать что-то другое*', callback_data='buton3')
    keyboard.row(but1)
    keyboard.add(but2)
    keyboard.add(but3)

    bot.send_photo(call.message.chat.id, open('photo/tokyo1_lvl3.jpg', 'rb'), caption=text['tokyo1 lvl3'], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'buton1')# локация tokyo1, lvl 4
def buton1(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, text= text['tokyo1 lvl4'])

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'buton2')# локация tokyo2, lvl 4
def buton2(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id,text=text['tokyo2 lvl4'])

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'buton3')# локация tokyo3, lvl 4
def buton3(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id,text=text['tokyo3 lvl4'])
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'buttt2')# локация tokyo2, lvl 2
def buttt2(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, text=text['tokyo2 lvl2'])
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'buttt3')# локация tokyo3, lvl 3
def buttt3(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'tokyo3'
    players[user_id]['lvl'] = "3"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('*солгать ему*', callback_data='butot1')
    but2 = types.InlineKeyboardButton('*сказать правду*', callback_data='butot2')
    but3 = types.InlineKeyboardButton('*извиниться за то, что побеспокоили его*', callback_data='butot3')
    keyboard.row(but1)
    keyboard.add(but2)
    keyboard.add(but3)

    bot.send_photo(call.message.chat.id, open('photo/tokyo3_lvl3.jpg', 'rb'), caption=text['tokyo3 lvl3'], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'butot1')# локация tokyo1, lvl 5
def butot1(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, text=text['tokyo1 lvl5'])
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'butot2')# локация tokyo2, lvl 5
def butot2(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, text=text['tokyo2 lvl5'])
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'butot3')# локация tokyo3, lvl 5
def butot3(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, text=text['tokyo3 lvl5'])
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'butonss3')
def butonss3(call):# локация 3 hero lvl 2
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = '3 hero'
    players[user_id]['lvl'] = "2"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Пойти вперёд', callback_data='butttt1')
    but2 = types.InlineKeyboardButton('Остаться на месте', callback_data='butttt2')
    keyboard.row(but1)
    keyboard.add(but2)

    bot.send_photo(call.message.chat.id, open('photo/3_hero.png', 'rb'), caption= text['3hero lvl2'], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'butttt1')
def butttt1(call):# локация 3 hero1 lvl 3
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = '3 hero1'
    players[user_id]['lvl'] = "3"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton("Пройти в крепость", callback_data='buttons1')
    but2 = types.InlineKeyboardButton('Остаться на опушке леса', callback_data='buttons2')
    but3 = types.InlineKeyboardButton('Пойти дальше исследовать мир', callback_data='')
    keyboard.add(but1)
    keyboard.add(but2)
    keyboard.add(but3)

    bot.send_photo(call.message.chat.id, open("photo/3_hero2.png", 'rb'), caption=text['3hero1 lvl3'], reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'buttons1')
def buttons1(call):# локация 3 hero1 lvl 4
    user_id = call.message.chat.id
    bot.send_message(call.message.chat.id, text=text['3hero1 lvl4'])
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)


@bot.callback_query_handler(func=lambda call: call.data == 'buttons2')
def buttons2(call):# локация 3 hero2 lvl 4
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, text=text['3hero2 lvl4'])

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'buttons3')
def buttons3(call):# локация 3 hero3 lvl 4
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, text = text['3hero3 lvl4'])

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)


@bot.callback_query_handler(func=lambda call: call.data == 'butttt2')
def handle_next_level_butttt2(call):  # локация 3 hero2 lvl 3
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, text=text['3hero2 lvl3'])

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('osnova/player.json', 'w+') as file:
        json.dump(players, file)

bot.polling()
