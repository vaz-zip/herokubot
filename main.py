import telebot
from telebot import types
from config import TOKEN
from extension import APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'], content_types=['text', ])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Багет'))
    markup.add(types.KeyboardButton('Бородинский'))
    markup.add(types.KeyboardButton('Зерновой'))
    markup.add(types.KeyboardButton('Тыквенный'))
    markup.add(types.KeyboardButton('Фитнес'))
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, с вами Хлеб-бот!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    

def on_click(message):
    if message.text == 'Багет':
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, Введите количество")
        bot.register_next_step_handler(message, baguette)
    elif message.text == 'Бородинский':
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, Введите количество")
        bot.register_next_step_handler(message, borodinsky )
    elif message.text == 'Зерновой':
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, Введите количество")
        bot.register_next_step_handler(message, grain )   
    elif message.text == 'Тыквенный':
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, Введите количество")
        bot.register_next_step_handler(message, pumpkin )      


def baguette(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 1:
            raise APIException('Значение должно быть одно!')
        persons = values
        person = int(''.join(map(str, persons)))
    except APIException as e:
        bot.reply_to(message, f'Ошибка!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду!\nВведите целое число!\nОшибка: {e}')
    else:
        text = f'Количество буханок \
            \nБАГЕТА: {person} \
            \nМука В/С....{person * 125} грамм,\
            \nМука 1с......{person * 102} грамм,\
            \nВода............{person * 160} грамм,\
            \nЗакваска....{person * 15} грамм,\
            \nСоль............{person * 5} грамм,\
            \nДобавки.....{person * 20} грамм'
        bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(message, on_click)


def borodinsky(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 1:
            raise APIException('Знвчение должно быть одно!')
        persons = values
        person = int(''.join(map(str, persons)))
    except APIException as e:
        bot.reply_to(message, f'Ошибка!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду!\nВведите целое число!\nОшибка: {e}')
    else:
        text = f'Количество буханок\
            \nБОРОДИНСКОГО: {person}\
            \nМука В/С....{person * 125} грамм,\
            \nМука 1с......{person * 102} грамм,\
            \nВода............{person * 160} грамм,\
            \nЗакваска....{person * 15} грамм,\
            \nСоль............{person * 5} грамм,\
            \nДобавки.....{person * 20} грамм'
        bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(message, on_click)


def grain(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 1:
            raise APIException('Знвчение должно быть одно!')
        persons = values
        person = int(''.join(map(str, persons)))
    except APIException as e:
        bot.reply_to(message, f'Ошибка!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду!\nВведите целое число!\nОшибка: {e}')
    else:
        text = f'Количество буханок\
            \nЗЕРНОВОГО: {person}\
            \nМука В/С....{person * 125} грамм,\
            \nМука 1с......{person * 102} грамм,\
            \nВода............{person * 160} грамм,\
            \nЗакваска....{person * 15} грамм,\
            \nСоль............{person * 5} грамм,\
            \nДобавки.....{person * 20} грамм'
        bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(message, on_click)


# @bot.message_handler(content_types=['text', ])
# def get_user_text(message: telebot.types.Message):
#     if message.text == '1': 
#         mess = f'Привет, <b>{message.from_user.first_name}! <u> Я рецепт №1, введите количество буханок</u></b>'
#         bot.send_message(message.chat.id, mess, parse_mode='html')
#     elif message.text == '2':
#         mess1 = f'Привет, <b>{message.from_user.first_name}! <u> Я рецепт №2</u></b>'
#         bot.send_message(message.chat.id, mess1, parse_mode='html')
#     elif message.text == '3':
#         mess2 = f'Привет, <b>{message.from_user.first_name}! <u> Я рецепт №2, Введи чило булок</u></b>'
#         bot.send_message(message.chat.id, mess2, parse_mode='html')

            





    
   


# @bot.message_handler(content_types=['text', ])
def pumpkin(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 1:
            raise APIException('Знвчение должно быть одно!')
        persons = values
        person = int(''.join(map(str, persons)))
    except APIException as e:
        bot.reply_to(message, f'Ошибка!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду!\nВведите целое число!\nОшибка: {e}')
    else:
        text = f'Количество буханок\
            \nТЫКВЕННОГО: {person} \
            \nМука В/С....{person * 125} грамм,\
            \nМука 1с......{person * 102} грамм,\
            \nВода............{person * 160} грамм,\
            \nЗакваска....{person * 15} грамм,\
            \nСоль............{person * 5} грамм,\
            \nДобавки.....{person * 20} грамм'
        bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(message, on_click)

bot.polling(non_stop=True)
