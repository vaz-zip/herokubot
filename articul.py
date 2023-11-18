import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

def articul(message, art):
    bot.send_message(message.chat.id, f"{message.from_user.first_name}, введите количество.")
    bot.register_next_step_handler(message, art)