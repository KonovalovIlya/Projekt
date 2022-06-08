import threading
import functools
import telebot
from telebot import types
from Parser import parsing
import settings
from settings import info, dict_
import re
import sqlite3 as db
from sqlite3 import Error


with db.connect('bot_db') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS USERS (chat_id INTEGER NOT NULL PRIMARY KEY, logfile TEXT, '
                   'command TEXT, city TEXT, range_price TEXT, range_distance TEXT, amount TEXT, photo_amount TEXT, '
                   'check_in TEXT, check_out TEXT)')


def send_user_info(chat_id=None, logfile=None, command=None, city=None, range_price=None, range_distance=None,
                   amount=None, photo_amount=None, check_in=None, check_out=None):
    connection = db.connect('bot_db')
    cursor = connection.cursor()
    try:
        if chat_id:
            cursor.execute(f'INSERT INTO USERS (chat_id) VALUES({chat_id})')
        elif logfile:
            cursor.execute(f'INSERT INTO USERS (logfile) VALUES({logfile})')
        elif command:
            cursor.execute(f'INSERT INTO USERS (command) VALUES({command})')
        elif city:
            cursor.execute(f'INSERT INTO USERS (city) VALUES({city})')
        elif range_price:
            cursor.execute(f'INSERT INTO USERS (range_price) VALUES({range_price})')
        elif range_distance:
            cursor.execute(f'INSERT INTO USERS (range_distance) VALUES({range_distance})')
        elif amount:
            cursor.execute(f'INSERT INTO USERS (amount) VALUES({amount})')
        elif photo_amount:
            cursor.execute(f'INSERT INTO USERS (photo_amount) VALUES({photo_amount})')
        elif check_in:
            cursor.execute(f'INSERT INTO USERS (check_in) VALUES({check_in})')
        elif check_out:
            cursor.execute(f'INSERT INTO USERS (check_out) VALUES({check_out})')
    except Error:
        pass
    connection.commit()
    connection.close()


bot = telebot.TeleBot(settings.KEY)

@bot.message_handler(commands=['start'])
def welcome(message):
    '''
    Приветствует пользователя
    '''
    # # global \
    # print('Словарь перед добавлением пользователя:', dict_)
    # dict_[str(message.chat.id)] = info
    # print('Словарь после добавления пользователя:', dict_)
    # dict_.get(str(message.chat.id))['log_file'] = str(message.chat.id).join(['log_', '.txt'])
    # print('Словарь после добавления лог-файла:', dict_)
    send_user_info(chat_id=message.chat.id, logfile=str(message.chat.id).join(['log_', '.txt']))

    bot.send_message(message.chat.id,
                     'Привет, {name}!\nНе знаешь с чего начать?\nХочешь узнать что я могу?\nНажми кнопку Help. '
                     'Или выбери другую команду.'.format(name=message.from_user.first_name))
    start_key_board(message)


@bot.message_handler(content_types=['text'])
def start_key_board(message):
    '''
    Вызывает клавиатуру выбора команд
    '''
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Могу найти отели:'
    keyboard.row(
        types.InlineKeyboardButton(text='Дешовые', callback_data='/lowprice'),
        types.InlineKeyboardButton(text='Дорогие', callback_data='/highprice'),
        types.InlineKeyboardButton(text='Для вас', callback_data='/bestdeal')
    )
    keyboard.row(
        types.InlineKeyboardButton(text='Help', callback_data='/help'),
        types.InlineKeyboardButton(text='History', callback_data='/history'),
    )
    bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_message(message):
    '''
    Выводит описание возможностей бота
    '''
    help_message_str = 'Я могу подбирать отели.\nЕсли нажмешь на кнопку "Дешовые", я подберу самые дешовые отели.\n'\
        'Если нажмешь на кнопку "Дорогие", я подберу самые дорогие отели.\nЕсли нажмешь на кнопку "Для вас", '\
        'я подберу самые подходящие отели под указанные параметры.\nЕсли нажмешь на кнопку "History", я отправлю '\
        'тебе файл с ответами на все запросы которые ты мне отправлял.\n'
    bot.send_message(message.chat.id, help_message_str)

    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Не забудь отправить коммент автору. Для поиска отелей нажми "Начать поиск"'
    keyboard.row(
        types.InlineKeyboardButton(text='Написать автору', url='telegram.me/AuthorTB'),
        types.InlineKeyboardButton(text='Начать поиск', callback_data='start_search')
    )
    bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)


@bot.message_handler(commands=['history'])
def history(message):
    '''
    История запросов.
    '''
    bot.send_document(message.chat.id, open(dict_.get(str(message.chat.id)).get('log_file'), 'rb'))


@bot.message_handler(content_types=['text'])
def get_city(message):
    """
    Город, где будет проводиться поиск.
    """
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'В каком городе подобрать отель?'
    keyboard.row(
        types.InlineKeyboardButton(text='London', callback_data='London'),
        types.InlineKeyboardButton(text='New York', callback_data='New York'),
        types.InlineKeyboardButton(text='Paris', callback_data='Paris')
    )
    keyboard.row(
        types.InlineKeyboardButton(text='Укажите свой вариант', callback_data='my_city'),
    )
    bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_range_price(message):
    """
    Определяет диапазон цен за номер за ночь
    """
    # global dict_
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Укажите стоимость номера за ночь'
    keyboard.row(
        types.InlineKeyboardButton(text='До 25', callback_data='0, 25'),
        types.InlineKeyboardButton(text='От 25 до 75', callback_data='25, 75'),
        types.InlineKeyboardButton(text='От 75 до 150', callback_data='75, 150'),
    )
    keyboard.row(
        types.InlineKeyboardButton(text='От 150 до 250', callback_data='150, 250'),
        types.InlineKeyboardButton(text='От 250 до 500', callback_data='250, 500')
    )
    try:
        if message.text.isascii():
            send_user_info(city=message.text)
            bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, 'В названии города используйте только латинские буквы')
            bot.register_next_step_handler(message, get_city)
    except:
        bot.send_message(message.message.chat.id, text=key_message, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_range_distance(message):
    """
    Определяет максимальное расстояние от центра
    """
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Укажите расстояние от центра в милях.'
    keyboard.row(
        types.InlineKeyboardButton(text='1', callback_data='dist_1'),
        types.InlineKeyboardButton(text='2', callback_data='dist_2'),
        types.InlineKeyboardButton(text='3', callback_data='dist_3'),
        types.InlineKeyboardButton(text='4', callback_data='dist_4'),
        types.InlineKeyboardButton(text='5', callback_data='dist_5')
    )
    bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_amount(message):
    """
    Определяет количество отелей по которым необходимо собрать информацию
    """
    # global dict_
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Укажите кол-во отелей.'
    keyboard.row(
        types.InlineKeyboardButton(text='1', callback_data='amount_1'),
        types.InlineKeyboardButton(text='2', callback_data='amount_2'),
        types.InlineKeyboardButton(text='3', callback_data='amount_3'),
        types.InlineKeyboardButton(text='4', callback_data='amount_4'),
        types.InlineKeyboardButton(text='5', callback_data='amount_5')
    )
    try:
        if message.text.isascii():
            send_user_info(city=message.text)
            bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, 'В названии города используйте только латинские буквы')
            bot.register_next_step_handler(message, get_city)
    except:
        bot.send_message(message.message.chat.id, text=key_message, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_date(message):
    """
    Определяет период за который необходимо
    """
    bot.send_message(message.chat.id, 'Укажите даты въезда и выезда через запятую в формате гггг-мм-дд')
    bot.register_next_step_handler(message, get_photo)


@bot.message_handler(content_types=['text'])
def get_photo(message):
    """
    Определяет необходимость загрузки фото
    """
    # global dict_
    if re.match(r'\d{4}-[0-1][0-9]-[0-3][0-9], \d{4}-[0-1][0-9]-[0-3][0-9]', message.text):
        send_user_info(check_in=message.text.split(', ')[0], check_out=message.text.split(', ')[1])
        # dict_.get(str(message.chat.id))['check_in'] = message.text.split(', ')[0]
        # dict_.get(str(message.chat.id))['check_out'] = message.text.split(', ')[1]
        # print(dict_)
        keyboard = types.InlineKeyboardMarkup()
        key_message = 'Загрузить фото по отелям?'
        keyboard.row(
            types.InlineKeyboardButton(text='Да', callback_data='yes_p'),
            types.InlineKeyboardButton(text='Нет', callback_data='no_p')
        )
        bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)
    else:
        bot.send_message(
            message.chat.id,
            'Проверьте указанные даты. Укажите даты въезда и выезда через запятую в формате гггг-мм-дд'
        )
        bot.register_next_step_handler(message, get_photo)


@bot.message_handler(content_types=['text'])
def get_photo_amount(message):
    """
    Определяет кол-во фото.
    """
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Укажите кол-во фото.'
    keyboard.row(
        types.InlineKeyboardButton(text='1', callback_data='photo_1'),
        types.InlineKeyboardButton(text='2', callback_data='photo_2'),
        types.InlineKeyboardButton(text='3', callback_data='photo_3'),
        types.InlineKeyboardButton(text='4', callback_data='photo_4'),
        types.InlineKeyboardButton(text='5', callback_data='photo_5')
    )
    bot.send_message(message.message.chat.id, text=key_message, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_confirmation(message):
    """
    Проверка запрашиваемых даных.
    """
    with db.connect('bot_db') as c:
        cursor = c.cursor()
        cursor.execute('SELECT * FROM USERS')
        res = cursor.fetchall()
        print(res)
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='Yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='No')
    keyboard.add(key_no)
    info_all = 'Ищем {amount} отелей в городе {city} с {photo_amount} фото'.format(
        amount=dict_.get(str(message.chat.id))['amount'],
        city=dict_.get(str(message.chat.id))['city'],
        photo_amount=dict_.get(str(message.chat.id))['photo_amount']
    )
    bot.send_message(message.chat.id, text=info_all, reply_markup=keyboard)


def restart(message):
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Для нового поиска нажми "Начать поиск"'
    keyboard.row(
        types.InlineKeyboardButton(text='Начать поиск', callback_data='start_search')
    )
    bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    """
    Обработка запроса.
    """
    # global dict_
    if call.data == "/help":
        bot.answer_callback_query(call.id)
        help_message(call.message)

    elif call.data == "/history":
        bot.answer_callback_query(call.id)
        history(call.message)
    else:
        bot.send_message(call.message.chat.id, 'Ok')

        if call.data == "/lowprice":
            bot.answer_callback_query(call.id)
            send_user_info(command='lowprice')
            get_city(call.message)

        elif call.data == 'start_search':
            bot.answer_callback_query(call.id)
            start_key_board(call.message)

        elif call.data == "/highprice":
            bot.answer_callback_query(call.id)
            send_user_info(command='highprice')
            get_city(call.message)

        elif call.data == "/bestdeal":
            bot.answer_callback_query(call.id)
            send_user_info(command='bestdeal')
            get_city(call.message)

        elif call.data in ['London', 'New York', 'Paris']:
            bot.answer_callback_query(call.id)
            send_user_info(city=call.data)
            # if dict_.get(str(call.chat.id))['command'] == 'bestdeal':
            #     get_range_price(call)
            # else:
            get_amount(call)

        # elif call.data == 'my_city':
        #     bot.answer_callback_query(call.id)
        #     if dict_.get(str(call.chat.id))['command'] == 'bestdeal':
        #         bot.register_next_step_handler(call.message, get_range_price)
        #     else:
        #         bot.register_next_step_handler(call.message, get_amount)

        elif re.search(r'\d{,3}, \d{,3}', call.data):
            bot.answer_callback_query(call.id)
            send_user_info(range_price=call.data.split(', '))
            get_range_distance(call.message)

        elif call.data.startswith('dist_'):
            bot.answer_callback_query(call.id)
            send_user_info(range_distance=call.data.lstrip('dist_'))
            get_amount(call)

        elif call.data.startswith('amount_'):
            bot.answer_callback_query(call.id)
            send_user_info(amount=call.data.lstrip('amount_'))
            get_date(call.message)

        elif call.data.startswith('photo_'):
            bot.answer_callback_query(call.id)
            send_user_info(photo_amount=call.data.lstrip('photo_'))
            get_confirmation(call)

        elif call.data == "Yes":
            bot.answer_callback_query(call.id)
            res = parsing(dict_.get(str(call.chat.id)))
            amount = len(res)
            print(res)
            if res == []:
                bot.send_message(call.message.chat.id, 'Я не смог ничего найти')
                restart(call.message)
            else:
                if '$' in res[0][4]:
                    bot.send_message(call.message.chat.id, 'Я смог найти {} из {} отелей'.format(
                        amount,
                        dict_[str(call.chat.id)].get('amount')
                    ))
                    for i in range(amount):
                        bot.send_message(
                            call.message.chat.id,
                            'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
                            'цена за ночь - {price}, стоимость за указанные даты - {price_for_all}, {photos}'.format(
                                name=res[i][0],
                                street=res[i][1],
                                distance=res[i][2],
                                price=res[i][3],
                                price_for_all=res[i][4],
                                photos=', '.join(res[i][5:])
                            ))
                    restart(call.message)
                else:
                    for i in range(amount):
                        bot.send_message(
                            call.message.chat.id,
                            'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
                            'цена за ночь - {price}, {photos}'.format(
                                name=res[i][0],
                                street=res[i][1],
                                distance=res[i][2],
                                price=res[i][3],
                                photos=', '.join(res[i][4:])
                            ))
                    restart(call.message)

        elif call.data == "No":
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, 'Начнем сначала')
            start_key_board(call.message)

        elif call.data == 'yes_p':
            bot.answer_callback_query(call.id)
            get_photo_amount(call)

        elif call.data == 'no_p':
            bot.answer_callback_query(call.id)
            send_user_info(photo_amount=0)
            get_confirmation(call)


if __name__ == '__main__':
    bot.polling(none_stop=True)
