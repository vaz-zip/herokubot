import telebot
from config import TOKEN
from extension import APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Введите необходимое количество буханок!'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 1:
            raise APIException('Знвчение должно быть одно!')
        persons = values

        person = int(''.join(map(str, persons)))
        print(person)
    except APIException as e:
        bot.reply_to(message, f'Ошибка!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду!\nВведите целое число!')
    else:
        text = f'Ha {person} буханок:\
               \nМука В/С....{person*125} грамм,\
               \nМука 1с......{person*102} грамм,\
               \nВода............{person*160} грамм,\
               \nЗакваска....{person*15} грамм,\
               \nСоль............{person*5} грамм,\
               \nДобавки.....{person*20} грамм.'
        bot.send_message(message.chat.id, text)


bot.polling()
