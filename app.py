import os
from dotenv import load_dotenv
import telebot

load_dotenv()
bot = telebot.TeleBot(os.getenv('API'))


@bot.message_handlers(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<a>Привет</a>', parse_mode='html')

