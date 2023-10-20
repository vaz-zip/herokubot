import telebot
from telebot import types
from config import TOKEN
from extension import APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'], content_types=['text', ])
def start(message):
    # mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}!</u></b>\
        # \nвыберите нужный рецепт! '
    # mess = f'{message.from_user.first_name}, выберите нужный рецепт!'
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Багет'))
    markup.add(types.KeyboardButton('Тыквенный'))
    markup.add(types.KeyboardButton('Чиабатта'))
    markup.add(types.KeyboardButton('Зерновой'))
    markup.add(types.KeyboardButton('Фитнес'))
    markup.add(types.KeyboardButton('Бородинский'))
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', reply_markup=markup)
    if message.text == 'Тыквенный':
         bot.register_next_step_handler(message, pumpkin)
    if message.text == 'Багет':
         bot.register_next_step_handler(message, pumpkin)     
    #      pumpkin()  
         
    
        # bot.reply_to(message, mess)
        # bot.register_message_handler(message, convert)
    # bot.register_next_step_handler(message, convert)
    # bot.send_message(message.chat.id, mess, parse_mode='html')

# @bot.message_handler(content_types=['text', ])
# def get_text(message):
#     if message.text == '9999':
#         mess = f'{message.from_user.first_name}, выберите нужный рецепт!'
#         markup = types.ReplyKeyboardMarkup()
#         markup.add(types.KeyboardButton('Багет'))
#         markup.add(types.KeyboardButton('Тыквенный'))
#         markup.add(types.KeyboardButton('Чиабатта'))
#         markup.add(types.KeyboardButton('Зерновой'))
#         markup.add(types.KeyboardButton('Фитнес'))
#         markup.add(types.KeyboardButton('Бородинский'))
#         bot.send_message(message, mess, message.chat.id, reply_markup=markup)
#         # bot.reply_to(message, mess)
#         # bot.register_message_handler(message, convert)
#         bot.register_next_step_handler(message, convert)


# @bot.message_handler(content_types=['text', ])
def baguette(message: telebot.types.Message):
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
            text = f'Количество буханок: {person}\
                \nМука В/С....{person * 125} грамм,\
                \nМука 1с......{person * 102} грамм,\
                \nВода............{person * 160} грамм,\
                \nЗакваска....{person * 15} грамм,\
                \nСоль............{person * 5} грамм,\
                \nДобавки.....{person * 20} грамм,\
                \nРецептура БАГЕТ'
            bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text', ])
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
             text = f'Количество буханок: {person}\
                \nМука В/С....{person * 125} грамм,\
                \nМука 1с......{person * 102} грамм,\
                \nВода............{person * 160} грамм,\
                \nЗакваска....{person * 15} грамм,\
                \nСоль............{person * 5} грамм,\
                \nДобавки.....{person * 20} грамм,\
                \nРецептура Тыквенный'
             bot.send_message(message.chat.id, text)

   
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'recept1':
#         try:
#             values = message.text.split(' ')
#             if len(values) != 1:
#                 raise APIException('Знвчение должно быть одно!')
#             persons = values
#             person = int(''.join(map(str, persons)))
#         except APIException as e:
#             bot.reply_to(message, f'Ошибка!\n{e}')
#         except Exception as e:
#             bot.reply_to(message, f'Не удалось обработать команду!\nВведите целое число!\nОшибка: {e}')
#         else:
#             text = f'Количество буханок: {person}\
#                \nМука В/С....{person * 125} грамм,\
#                \nМука 1с......{person * 102} грамм,\
#                \nВода............{person * 160} грамм,\
#                \nЗакваска....{person * 15} грамм,\
#                \nСоль............{person * 5} грамм,\
#                \nДобавки.....{person * 20} грамм,\
#                \nМВУУУ-ХА-ХА-ХА! I`am CRAGY-DACK !!'
#             bot.send_message(message.chat.id, text)



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
