import telebot
from telebot import types
from Parser import parsing
import requests


bot = telebot.TeleBot('5246923628:AAGR1ONt2gFZ8vQoqz6I4TpL7cAiPVaNQfg')
info = dict()

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, {name}!'.format(name=message.from_user.first_name))


@bot.message_handler(commands=['lowprice'])
def lowprice(message):
    bot.send_message(message.chat.id, 'Давайте начнем')
    get_message(message)

@bot.message_handler(content_types=['text'])
def get_message(message):
    # Город, где будет проводиться поиск.
    bot.send_message(message.chat.id, 'В каком городе подобрать отель?')
    bot.register_next_step_handler(message, get_city)

def get_city(message):
    info['city'] = message.text
    bot.send_message(message.chat.id, 'Укажите кол-во отелей (не больше пяти)')
    bot.register_next_step_handler(message, get_amount)

def get_amount(message):
    global info
    # 2. Количество отелей, которые необходимо вывести в результате(не больше заранее определённого максимума).
    # bot.send_message(message.chat.id, 'Укажите кол-во отелей (не больше пяти)')
    # while int(message.text) > 5:
    #     bot.send_message(message.chat.id, 'Кол-во отелей должно быть не больше пяти)')
    info['amount'] = message.text
    bot.send_message(message.chat.id, 'Укажите даты въезда и выезда через запятую в формате гггг-мм-дд')
    bot.register_next_step_handler(message, get_date)


def get_date(message):
    global info
    info['check_in'] = message.text.split(', ')[0]
    info['check_out'] = message.text.split(', ')[1]
    bot.send_message(message.chat.id, 'Загрузить фото по отелям?')
    bot.register_next_step_handler(message, get_foto)

def get_foto(message):
    if message.text == 'Да':
    # 3. Необходимость загрузки и вывода фотографий для каждого отеля(“Да / Нет”)
    # bot.send_message(message.chat.id, 'Загрузить фото по отелям?')
        bot.send_message(message.chat.id, 'Сколько фото(не больше пяти)?')
        bot.register_next_step_handler(message, get_foto_amount)
    else:
        bot.register_next_step_handler(message, get_foto_amount)


def get_foto_amount(message):
    global info
    # if message.text == 'Да':
        # bot.send_message(message.chat.id, 'Сколько фото(не больше пяти)?')
    info['foto_amount'] = int(message.text)
        # a.При положительном ответе пользователь также вводит количество необходимых фотографий(не больше заранее
        #         определённого максимума)
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='Yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='No')
    keyboard.add(key_no)
    info_all = 'Ищем {amount} отелей в городе {city} с {foto_amount} фото'.format(
        amount=info['amount'],
        city=info['city'],
        foto_amount=info['foto_amount']
    )
    bot.send_message(message.from_user.id, text=info_all, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global info
    if call.data == "Yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        res = parsing(info)#код сохранения данных, или их обработки
        for i in range(3):
            bot.send_message(
                call.message.chat.id, 'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
                                      'цена за ночь - {price}, стоимость за указанные даты - {price_for_all}'.format(
                    name=res[i][0],
                    street=res[i][1],
                    distance=res[i][2],
                    price=res[i][3],
                    price_for_all=res[i][4]
                ))
    elif call.data == "No":
         pass #переспрашиваем

if __name__ == '__main__':
    bot.polling(none_stop=True)
