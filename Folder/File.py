import telebot
import requests


bot = telebot.TeleBot('5246923628:AAGR10Nt2gFZ8vQoqz6I4TpL7cAiPVaNQfg')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, {name}!'.format(name=message.from_user))

bot.polling(none_stop=True)
