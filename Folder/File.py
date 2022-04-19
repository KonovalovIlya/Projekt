import telebot
from telebot import types
from Parser import parsing
import settings
import re


bot = telebot.TeleBot(settings.KEY)
info = dict()


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, {name}!'.format(name=message.from_user.first_name))


@bot.message_handler(commands=['lowprice'])
def lowprice(message):
    '''
    Подбирает самые дешовые отели.
    '''
    bot.send_message(message.chat.id, 'Давайте начнем')
    get_message(message)


@bot.message_handler(content_types=['text'])
def get_message(message):
    """
    Город, где будет проводиться поиск.
    """
    bot.send_message(message.chat.id, 'В каком городе подобрать отель?')
    bot.register_next_step_handler(message, get_city)


@bot.message_handler(content_types=['text'])
def get_city(message):
    """
    Определяет количество отелей оп которым необходимо собрать информацию
    """
    if message.text.isascii():
        info['city'] = message.text
        bot.send_message(message.chat.id, 'Укажите кол-во отелей (не больше пяти)')
        bot.register_next_step_handler(message, get_amount)
    else:
        bot.send_message(message.chat.id, 'В названии города используйте только латинские буквы')
        get_message(message)


@bot.message_handler(content_types=['text'])
def get_amount(message):
    """
    Определяет период за который необходимо
    """
    if message.text.isdigit():
        info['amount'] = message.text
        bot.send_message(message.chat.id, 'Укажите даты въезда и выезда через запятую в формате гггг-мм-дд')
        bot.register_next_step_handler(message, get_date)
    else:
        bot.send_message(message.chat.id, 'Используйте цифры')
        bot.register_next_step_handler(message, get_amount)


@bot.message_handler(content_types=['text'])
def get_date(message):
    """
    Определяет необходимость загрузки фото
    """
    if re.match(r'\d{4}-[0-1][0-9]-[0-3][0-9], \d{4}-[0-1][0-9]-[0-3][0-9]', message.text):
        info['check_in'] = message.text.split(', ')[0]
        info['check_out'] = message.text.split(', ')[1]
        bot.send_message(message.chat.id, 'Загрузить фото по отелям?')
        bot.register_next_step_handler(message, get_photo)
    else:
        bot.send_message(
            message.chat.id,
            'Проверьте указанные даты. Укажите даты въезда и выезда через запятую в формате гггг-мм-дд'
        )
        bot.register_next_step_handler(message, get_date)


@bot.message_handler(content_types=['text'])
def get_photo(message):
    """
    Определяет кол-во фото.
    """
    if message.text == 'Да':
        bot.send_message(message.chat.id, 'Сколько фото(не больше пяти)?')
        bot.register_next_step_handler(message, get_photo_amount)
    else:
        bot.register_next_step_handler(message, get_photo_amount)


@bot.message_handler(content_types=['text'])
def get_photo_amount(message):
    """
    Проверка запрашиваемых даных.
    """
    if message.text.isdigit():
        info['photo_amount'] = int(message.text)
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='Yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='No')
        keyboard.add(key_no)
        info_all = 'Ищем {amount} отелей в городе {city} с {photo_amount} фото'.format(
            amount=info['amount'],
            city=info['city'],
            photo_amount=info['photo_amount']
        )
        bot.send_message(message.from_user.id, text=info_all, reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'Используйте цифры')
        bot.register_next_step_handler(message, get_photo)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    """
    Обработка запроса.
    """
    if call.data == "Yes":
        res = parsing(info)
        if '$' in res[0][4]:
            for i in range(int(info.get('amount'))):
                bot.send_message(
                    call.message.chat.id, 'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
                    'цена за ночь - {price}, стоимость за указанные даты - {price_for_all}, {photos}'.format(
                        name=res[i][0],
                        street=res[i][1],
                        distance=res[i][2],
                        price=res[i][3],
                        price_for_all=res[i][4],
                        photos=res[i][5:]
                    ))
        else:
            for i in range(int(info.get('amount'))):
                bot.send_message(
                    call.message.chat.id, 'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
                    'цена за ночь - {price}, {photos}'.format(
                        name=res[i][0],
                        street=res[i][1],
                        distance=res[i][2],
                        price=res[i][3],
                        photos=res[i][4:]
                    ))
    elif call.data == "No":
        bot.send_message(call.message.chat.id, 'Начнем сначала')
        get_message(call.message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
