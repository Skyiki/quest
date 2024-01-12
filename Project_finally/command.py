import telebot
import Osnova
import json
from telebot import types

bot = telebot.TeleBot(token=Osnova.token)

try:
    with open('player.json', 'r') as file:
        players = json.load(file)
except:
    players = {}


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
        if players[user_id]['location'] == 'start' and players[user_id]['lvl'] == "1":
            players[user_id] = {}
            players[user_id]['location'] = 'start'
            players[user_id]['lvl'] = "1"

            with open('player.json', 'w+') as file:
                json.dump(players, file)

            keyboard = types.InlineKeyboardMarkup()
            but1 = types.InlineKeyboardButton(text='Закричать', callback_data='but1')
            but2 = types.InlineKeyboardButton(text='Смириться', callback_data='but2')
            but3 = types.InlineKeyboardButton(text='Попытаться двигаться', callback_data='but3')
            keyboard.add(but1)
            keyboard.add(but2)
            keyboard.add(but3)

            bot.send_message(call.message.chat.id, "Вы чувствуете, что под вами нет твердой поверхности."
                                                   ' Вы открываете глаза, пытаясь понять, что происходит.'
                                                   ' Как только вы открываете глаза, то вас охватывает страх.'
                                                   'Вы падаете. Вы пытаетесь успокоиться и к счастью вам это удается.'
                                                   ' \nВы решаете', reply_markup=keyboard)
        elif players[user_id]['location'] == 'cat' and players[user_id]['lvl'] == "2":
            bot.register_next_step_handler_by_chat_id(user_id, butonss1)

        elif players[user_id]['location'] == 'cat1' and players[user_id]['lvl'] == "3":
            bot.register_next_step_handler_by_chat_id(user_id, butt1)

        elif players[user_id]['location'] == 'cat3' and players[user_id]['lvl'] == "3":
            bot.register_next_step_handler_by_chat_id(user_id, butt3)

        elif players[user_id]['location'] == 'tokyo' and players[user_id]['lvl'] == "2":
            bot.register_next_step_handler_by_chat_id(user_id, butonss2)

        elif players[user_id]['location'] == 'tokyo1' and players[user_id]['lvl'] == "3":
            bot.register_next_step_handler_by_chat_id(user_id, buttt1)

        elif players[user_id]['location'] == 'tokyo3' and players[user_id]['lvl'] == "3":
            bot.register_next_step_handler_by_chat_id(user_id, buttt3)

        elif players[user_id]['location'] == '3 hero' and players[user_id]['lvl'] == "2":
            bot.register_next_step_handler_by_chat_id(user_id, butonss3)

        elif players[user_id]['location'] == '3 hero1' and players[user_id]['lvl'] == "3":
            bot.register_next_step_handler_by_chat_id(user_id, butttt1)

    elif user_id not in players:
        players[user_id] = {}
        players[user_id]['location'] = 'start'
        players[user_id]['lvl'] = "1"

        with open('player.json', 'w+') as file:
            json.dump(players, file)

        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton(text='Закричать', callback_data='butonss1')
        but2 = types.InlineKeyboardButton(text='Смириться', callback_data='butonss2')
        but3 = types.InlineKeyboardButton(text='Попытаться двигаться', callback_data='butonss3')
        keyboard.add(but1)
        keyboard.add(but2)
        keyboard.add(but3)

        bot.send_message(call.message.chat.id,"Вы чувствуете, что под вами нет твердой поверхности."
                                                   ' Вы открываете глаза, пытаясь понять, что происходит.'
                                                   ' Как только вы открываете глаза, то вас охватывает страх.'
                                                   'Вы падаете. Вы пытаетесь успокоиться и к счастью вам это удается.'
                                                   ' \nВы решаете', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "button2")
def callback_Inlinee(call):
    bot.send_message(call.message.chat.id, 'Хорошо. Если передумаете, то нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'butonss1')# локация cat, lvl 2
def butonss1(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'cat'
    players[user_id]['lvl'] = "2"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Погладить', callback_data='butt1')
    but2 = types.InlineKeyboardButton('Взять кота на руки', callback_data='butt2')
    but3 = types.InlineKeyboardButton('Отойти подальше', callback_data='butt3')
    keyboard.row(but1)
    keyboard.add(but2)
    keyboard.add(but3)

    bot.send_message(call.message.chat.id,
                             'Как только вы начинаете кричать до вашего слуха доносится мяуканье кота.'
                             ' Вы перестаете кричать и понимаете, что находитесь на твердой поверхности,'
                             ' а рядом с вами сидит кот.'
                             ' Вы начинаете оглядываться и понимаете, что находитесь всё в том же белом пространстве,'
                             ' только почему-то вы стоите, а не падаете.'
                             ' В то время, пока вы оглядываетесь, кот смотрит на вас своими зелеными глазами,'
                             ' кажется он недоволен вашим криком.'
                             ' Вдруг, кот снова мяукает и смотрит на вас, ожидая реакции',
                             reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "butt1")# локация cat1, lvl 3
def butt1(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'cat1'
    players[user_id]['lvl'] = "3"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Тут нельзя оставаться. Пойти искать выход', callback_data='buut1')
    but2 = types.InlineKeyboardButton('Кот такой милый останусь с ним.', callback_data='buut2')
    keyboard.row(but1)
    keyboard.add(but2)

    bot.send_message(call.message.chat.id, 'Вы аккуратно гладите кота. Он начинает мурчать, покачивая хвостом'
                                           'Погладив кота, вы задумываетесь о том, где вы находитесь '
                                           'и что вам следует делать',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "buut1")# локация cat1, lvl 4
def buut1(call):
    user_id = call.message.chat.id
    bot.send_message(call.message.chat.id, 'Вы натыкаетесь на опасного зверя и он съедает вас. Вы проиграли!'
                                           '\nНажмите /start, чтобы начать игру заново.')

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == "buut2")# локация cat2, lvl 4
def buut2(call):
    user_id = call.message.chat.id
    bot.send_message(call.message.chat.id, 'Вы остаётесь с котом, думая, что он хороший.'
                                           ' Вот только он оказывается людоедом!'
                                           ' Вы проиграли, вас съел кот!'
                                           '\nНажмите /start, чтобы начать игру заново.')

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == "butt2")# локация cat2, lvl 3
def butt2(call):
    user_id = call.message.chat.id
    bot.send_message(call.message.chat.id, 'Коту не понравилось, что от вас пахнет цитрусами.'
                                           ' Он бъёт вас лапой, попадая по шеи.'
                                           ' Он случайно задевает жизненно-важные сосуды, и вы умираете,'
                                           ' истекая кровью.'
                                           ' Вы проиграли!'
                                           '\nНажмите /start, чтобы начать игру заново.')

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == "butt3")# локация cat3, lvl 3
def butt3(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'cat3'
    players[user_id]['lvl'] = "3"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Побежать в случайную сторону', callback_data='buuut1')
    but2 = types.InlineKeyboardButton('Остаться на месте', callback_data='buuut2')
    keyboard.row(but1)
    keyboard.add(but2)

    bot.send_message(call.message.chat.id, 'Вы решаете не приближаться к коту и отходите от него.'
                                           ' Вдруг, местность вокруг вас меняется, '
                                           'все вокруг переливается разными цветами. '
                                           'Местность сначала становится похожа на вулкан, '
                                           'после сменяется на океан, лес. '
                                           '\nВы решаете:',
                     reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "buuut1")# локация cat1, lvl 4
def buuut1(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, 'Вы побежали налево, пытаясь избегать препятствия, '
                                           'но всё равно упали в вулкан. \nВы проиграли!'
                                           '\nНажмите /start, чтобы начать игру заново.')

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)


@bot.callback_query_handler(func=lambda call: call.data == "buuut2")# локация cat2, lvl 4
def buuut2(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, 'Вы остаётесь на месте и вас накрывает волной цунами,'
                                           ' когда вы выплываете, то попадаете на гору. '
                                           'Местность перестаёт меняться, но на горе становится очень холодно,'
                                           ' так как ваша одежда всё ещё мокрая.'
                                           'Вы медленно умираете от обморожения. '
                                           '\nВы проиграли!'
                                           '\nНажмите /start, чтобы начать игру заново.')

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'butonss2')# локация tokyo, lvl 2
def butonss2(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'tokyo'
    players[user_id]['lvl'] = "2"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Заговорить с людьми', callback_data='buttt1')
    but2 = types.InlineKeyboardButton('Всё как-нибудь само решится', callback_data='buttt2')
    but3 = types.InlineKeyboardButton('Взять случайного прохожего за руку', callback_data='buttt3')
    keyboard.row(but1)
    keyboard.add(but2)
    keyboard.add(but3)

    bot.send_message(call.message.chat.id,
                             'Когда вы уже решаете смириться с этой ситуацией, вас что-то резко толкает вперед.'
                             ' Вы оказываетесь посреди оживленной улицы. Рядом с вами ходят множество людей. '
                             ' Вы оглядываетесь, вокруг вас полно пестрящих вывесок магазинов и много другого,'
                             ' но все они написаны на другом языке.'
                             ' Вот только почему-то вы отлично понимаете речь людей.'
                             ' Вам нужно что-то делать, чтобы разобраться в данной ситуации.',
                             reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'buttt1')# локация tokyo1, lvl 3
def buttt1(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'tokyo1'
    players[user_id]['lvl'] = "3"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('*сказать правду*', callback_data='buton1')
    but2 = types.InlineKeyboardButton('*сказать, что вы потеряли память*', callback_data='buton2')
    but3 = types.InlineKeyboardButton('*подкатить к мужчине*', callback_data='buton3')
    keyboard.row(but1)
    keyboard.add(but2)
    keyboard.add(but3)

    bot.send_message(call.message.chat.id,
                             'Вы окликаете мужчину, одетого в костюм. Он поворачивается.'
                             ' Его лицо кажется вам смутно знакомыми. Он недоумённо смотрят на вас.'
                             '\n- Мисс, вы что-то хотели? - мужчина подходит к вам, ожидая ответа.'
                             ' Он кажется недовольным'
                             ' тем, что кто-то тратит его время. Вам лучше поторопиться с ответом',
                             reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'buton1')# локация tokyo1, lvl 4
def buton1(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id,'Мужчина кажется заинтересован вашим рассказом.'
                                              ' Он поправляет свои очки.'
                                              'Он задаёт вам много уточняющих вопросов, понимая,'
                                              ' что ты говоришь ему правду'
                                              '\n- Я помогу тебе. - мужчина исполняет своё обещание. '
                                              '\nВы выиграли!'
                                              '\nНажмите /start, чтобы начать игру заново.')

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'buton2')# локация tokyo2, lvl 4
def buton2(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id,'Мужчина кажется заинтересован вашим рассказом.'
                                              ' Он поправляет свои очки.'
                                              'Он задаёт вам много уточняющих вопросов, понимая,'
                                              ' что ты говоришь ему неправду. '
                                              'Ему не понравилось, что ты зря потратил_а его время. Он убивает тебя'
                                              '\nВы проиграли!'
                                              '\nНажмите /start, чтобы начать игру заново.')

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'buton3')# локация tokyo3, lvl 4
def buton3(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id,'Мужчина нахмурился,'
                                              ' ему не понравилось, что ты зря потратил_а его время. Он убивает тебя'
                                              '\nВы проиграли!'
                                              '\nНажмите /start, чтобы начать игру заново.')
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'buttt2')# локация tokyo2, lvl 2
def buttt2(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, 'Вы наблюдаете за облаками, как вдруг, на вас падает здание.'
                                               ' \n Вы проиграли! \nНажмите /start, чтобы начать игру заново.')
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'buttt3')# локация tokyo3, lvl 3
def buttt3(call):
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = 'tokyo3'
    players[user_id]['lvl'] = "3"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('*сказать, что вы маг*', callback_data='butot1')
    but2 = types.InlineKeyboardButton('*сказать, что вы немаг*', callback_data='butot2')
    but3 = types.InlineKeyboardButton('*извиниться за то, что побеспокоили его*', callback_data='butot3')
    keyboard.row(but1)
    keyboard.add(but2)
    keyboard.add(but3)

    bot.send_message(call.message.chat.id, 'Вы берёте мужчину за руку. Он оборачивается и смотрит на вас. '
                                               'Вы узнаёте его. '
                             'Это персонаж из одного произведния - Гето Сугуру.'
                             '- Чего тебе? - вы вспоминаете, что он ненавидит всех немагов.'
                             ' Вам следует поторопиться с ответом, он готов убить вас в любой момент',
                             reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'butot1')# локация tokyo1, lvl 4
def butot1(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, 'Вы решаете солгать ему. Он это понял и убивает вас особенно болезнено'
                             ' \n Вы проиграли! \nНажмите /start, чтобы начать игру заново.')
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'butot2')# локация tokyo2, lvl 4
def butot2(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, 'Вы говорите ему правду. Он убивает вас. '
                                               'Вам не стоило приближаться к нему. \n Вы проиграли!'
                                               '\nНажмите /start, чтобы начать игру заново.')
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'butot3')# локация tokyo3, lvl 4
def butot3(call):
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, 'Вы извиняетесь перед ним, но ему уже всё равно. Он убивает вас.'
                                               ' \n Вы проиграли!'
                                               '\nНажмите /start, чтобы начать игру заново.')
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'butonss3')
def butonss3(call):# локация 3 hero lvl 2
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = '3 hero'
    players[user_id]['lvl'] = "2"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Пойти вперёд', callback_data='butttt1')
    but2 = types.InlineKeyboardButton('Остаться на месте', callback_data='butttt2')
    keyboard.row(but1)
    keyboard.add(but2)

    bot.send_message(call.message.chat.id,
                             'Вы пытаетесь двигаться, как вдруг, у вас перед глазами замелькало множество красок.'
                             ' Когда вы приходите в себя, то обнаруживаете густой лес. Ветви деревьев закрывают проход '
                             'к солнцу, из-за этого вы не можете далеко видеть.'
                             ' Из-за странной атмосферы вам становится страшно.'
                             ' Вы решаете:',
                             reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'butttt1')
def butttt1(call):# локация 3 hero1 lvl 3
    user_id = call.message.chat.id

    players[user_id] = {}
    players[user_id]['location'] = '3 hero1'
    players[user_id]['lvl'] = "3"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton("Пройти в крепость", callback_data='buttons1')
    but2 = types.InlineKeyboardButton('Остаться на опушке леса', callback_data='buttons2')
    but3 = types.InlineKeyboardButton('Пойти дальше исследовать мир', callback_data='')
    keyboard.add(but1)
    keyboard.add(but2)
    keyboard.add(but3)

    bot.send_message(call.message.chat.id, 'Вы решаете идти вперёд. Проходя сквозь густую чащу, вы видете'
                                           ' смутно знакомый замок, больше похожий на город или крепость. '
                                           'Вас влечёт к этому величественному строению. Вы решаете: ',
                     reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'buttons1')
def buttons1(call):# локация 3 hero1 lvl 4
    user_id = call.message.chat.id
    bot.send_message(call.message.chat.id, 'Вы проходите к крепость. Осматриваясь, вы замечаете как все тут красиво, '
                                           'но старомодно. Спустя долгое время скитаний вас жалеет один добрый человек.'
                                           ' Он приютил вас. Вы остались жить в этой крепости. '
                                           '\nВы остались жить в крепости! \nВы выиграли! ')
    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)


@bot.callback_query_handler(func=lambda call: call.data == 'buttons2')
def buttons2(call):# локация 3 hero2 lvl 4
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, 'Вы остаётесь на опушке леса. Разглядывая местность, вы обнаруживаете '
                                           'стаю диких волков. Они нападают на вас.'
                                           '\nВы проиграли! \nНажмите /start, чтобы начать игру заново.')

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

@bot.callback_query_handler(func=lambda call: call.data == 'buttons3')
def buttons3(call):# локация 3 hero3 lvl 4
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, 'Вы решаете исследовать этот мир, да вот только вы ничего о нём не знаете'
                                           '. Поэтому умираете в первый день вашего путешествия. '
                                           'На вас напали разбойники. \nВы проиграли! '
                                           '\nНажмите /start, чтобы начать игру заново.')

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)


@bot.callback_query_handler(func=lambda call: call.data == 'butttt2')
def handle_next_level_butttt2(call):  # локация 3 hero2 lvl 3
    user_id = call.message.chat.id

    bot.send_message(call.message.chat.id, 'Вы решаете остаться на месте, но быстро жалеете о своём решении.'
                                           'На вас нападают охотники, убивая. \nВы проиграли'
                                           '\nНажмите /start, чтобы начать игру заново.')

    players[user_id]['location'] = 'start'
    players[user_id]['lvl'] = "1"

    with open('player.json', 'w+') as file:
        json.dump(players, file)

bot.polling()
