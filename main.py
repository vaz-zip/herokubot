import telebot
from telebot import types
from config import TOKEN
from extension import APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def helper(message: telebot.types.Message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}!</u></b>\
        \nВведите 1 '
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(comands=['1'])
def get_text(message: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Багет', collback_data = 'recept1'))
    markup.add(types.InlineKeyboardButton('Багет', collback_data = 'recept2'))
    markup.add(types.InlineKeyboardButton('Багет', collback_data = 'recept3'))
    markup.add(types.InlineKeyboardButton('Багет', collback_data = 'recept4'))
    markup.add(types.InlineKeyboardButton('Багет', collback_data = 'recept5'))
    markup.add(types.InlineKeyboardButton('Багет', collback_data = 'recept6'))
    bot.reply_to(message, reply_markup = markup)


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
# def convert(message: telebot.types.Message):
#     try:
#         values = message.text.split(' ')
#         if len(values) != 1:
#             raise APIException('Знвчение должно быть одно!')
#         persons = values

#         person = int(''.join(map(str, persons)))

#     except APIException as e:
#         bot.reply_to(message, f'Ошибка!\n{e}')
#     except Exception as e:
#         bot.reply_to(message, f'Не удалось обработать команду!\nВведите целое число!\nОшибка: {e}')
#     else:
#         text = f'Количество буханок: {person}\
#                \nМука В/С....{person * 125} грамм,\
#                \nМука 1с......{person * 102} грамм,\
#                \nВода............{person * 160} грамм,\
#                \nЗакваска....{person * 15} грамм,\
#                \nСоль............{person * 5} грамм,\
#                \nДобавки.....{person * 20} грамм,\
#                \nМВУУУ-ХА-ХА-ХА! I`am CRAGY-DACK !!'
#         bot.send_message(message.chat.id, text)

bot.polling(non_stop=True)
