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


#    if user_id in players:

# Функция запустится, когда пользователь нажмет на кнопку
@bot.callback_query_handler(func=lambda call: call.data == "button1")# локация start, lvl 1
def callback_Inline(call):
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton(text='Закричать', callback_data='but1')
        but2 = types.InlineKeyboardButton(text='Смириться', callback_data='but2')
        but3 = types.InlineKeyboardButton(text='Попытаться двигаться', callback_data='but3')
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


@bot.callback_query_handler(func=lambda call: call.data == 'but1')
def handle_next_level_buttons(call):
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


@bot.callback_query_handler(func=lambda call: call.data == "butt1")
def callback_Inlines(call):
    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Тут нельзя оставаться. Пойти искать выход', callback_data='buut1')
    but2 = types.InlineKeyboardButton('Кот такой милый останусь с ним.', callback_data='buut2')
    keyboard.row(but1)
    keyboard.add(but2)

    bot.send_message(call.message.chat.id, 'Вы аккуратно гладите кота. Он начинает мурчать, покачивая хвостом'
                                           'Погладив кота, вы задумываетесь о том, где вы находитесь '
                                           'и что вам следует делать',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "buut1")
def callback_Inlines(call):
    bot.send_message(call.message.chat.id, 'Вы натыкаетесь на опасного зверя и он съедает вас. Вы проиграли!'
                                           '\nНажмите /start, чтобы начать игру заново.')

@bot.callback_query_handler(func=lambda call: call.data == "buut2")
def callback_Inlines(call):
    bot.send_message(call.message.chat.id, 'Вы остаётесь с котом, думая, что он хороший.'
                                           ' Вот только он оказывается людоедом!'
                                           ' Вы проиграли, вас съел кот!'
                                           '\nНажмите /start, чтобы начать игру заново.')

@bot.callback_query_handler(func=lambda call: call.data == "butt2")
def callback_Inlines(call):
    bot.send_message(call.message.chat.id, 'Коту не понравилось, что от вас пахнет цитрусами.'
                                           ' Он бъёт вас лапой, попадая по шеи.'
                                           ' Он случайно задевает жизненно-важные сосуды, и вы умираете,'
                                           ' истекая кровью.'
                                           ' Вы проиграли!'
                                           '\nНажмите /start, чтобы начать игру заново.')




@bot.callback_query_handler(func=lambda call: call.data == 'but2')
def handle_next_level_buttons(call):
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

@bot.callback_query_handler(func=lambda call: call.data == 'but3')
def handle_next_level_buttons(call):# локация 3 богатыря lvl 2
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Пойти вперёд', callback_data='butttt1')
        but2 = types.InlineKeyboardButton('Поискать что-нибудь', callback_data='butttt2')
        keyboard.row(but1)
        keyboard.add(but2)

        bot.send_message(call.message.chat.id,
                             'Вы пытаетесь двигаться, как вдруг, у вас перед глазами замелькало множество красок.'
                             ' Когда вы приходите в себя, то обнаруживаете густой лес. Ветви деервьев закрывают проход '
                             'к солнцу, из-за этого вы не можете далеко видеть.'
                             ' Из-за него вам становится страшно.'
                             ' Вы решаете:',
                             reply_markup=keyboard)


bot.polling()
