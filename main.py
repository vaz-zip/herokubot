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

def articul(message, art):
    bot.send_message(message.chat.id, f"{message.from_user.first_name}, Введите количество")
    bot.register_next_step_handler(message, art)


def on_click(message):
    if message.text == 'Багет':
        articul(art=baguette)
    elif message.text == 'Бородинский':
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, Введите количество")
        bot.register_next_step_handler(message, borodinsky )
    elif message.text == 'Зерновой':
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, Введите количество")
        bot.register_next_step_handler(message, grain )   
    elif message.text == 'Тыквенный':
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, Введите количество")
        bot.register_next_step_handler(message, pumpkin )
    elif message.text == 'Фитнес':
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, Введите количество")
        bot.register_next_step_handler(message, fitness )          


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
