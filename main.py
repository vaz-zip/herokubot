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
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, с вами Хлеб-бот 😄!\
                      \nВыберите в меню наменование хлеба!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def articul(message, art):
    bot.send_message(message.chat.id, f"{message.from_user.first_name}, введите количество.")
    bot.register_next_step_handler(message, art)


def on_click(message):
    if message.text == 'Багет':
        articul(message, baguette)
    elif message.text == 'Бородинский':
        articul(message, borodinsky)
    elif message.text == 'Зерновой':
        articul(message, grain)  
    elif message.text == 'Тыквенный':
        articul(message, pumpkin)
    elif message.text == 'Фитнес':
        articul(message, fitness)

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


def fitness(message: telebot.types.Message):
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
            \n`ФИТНЕС``: {person}\
            \nМука В/С....{person * 125} грамм,\
            \nМука 1с......{person * 102} грамм,\
            \nВода............{person * 160} грамм,\
            \nЗакваска....{person * 15} грамм,\
            \nСоль............{person * 5} грамм,\
            \nДобавки.....{person * 20} грамм'
        bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(message, on_click)


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






# def recipe(person, r_1, r_2, r_3, r_4, r_5, r_6 ):
#     text = f'Количество буханок \
#             \nБАГЕТА: {person} \
#             \nМука В/С....{person * r_1} грамм,\
#             \nМука 1с......{person * r_2} грамм,\
#             \nВода............{person * r_3} грамм,\
#             \nЗакваска....{person * r_4} грамм,\
#             \nСоль............{person * r_5} грамм,\
#             \nДобавки.....{person * r_6} грамм'
#         bot.send_message(message.chat.id, text)
#         bot.register_next_step_handler(message, on_click)
