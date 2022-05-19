import threading
import functools
import telebot
from telebot import types
from Parser import parsing
import settings
from settings import info, dict_
import re


bot = telebot.TeleBot(settings.KEY)


def threading_func(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        lock = threading.Lock()
        with lock:
            thread = threading.Thread(target=func(*args, **kwargs))
            thread.start()
            thread.join()
        return
    return wrapped


@bot.message_handler(commands=['start'])
@threading_func
def welcome(message):
    '''
    Приветствует пользователя
    '''
    global dict_
    dict_[str(message.from_user.id)] = info
    dict_.get(str(message.from_user.id))['log_file'] = str(message.from_user.id).join(['log_', '.txt'])
    print(dict_)
    bot.send_message(message.chat.id,
                     'Привет, {name}!\nНе знаешь с чего начать?\nХочешь узнать что я могу?\nНажми кнопку Help. '
                     'Или выбери другую команду.'.format(
                         name=message.from_user.first_name))
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
    bot.send_document(message.chat.id, open(dict_.get(str(message.from_user.id)).get('log_file'), 'rb'))


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
@threading_func
def get_range_price(message):
    """
    Определяет диапазон цен за номер за ночь
    """
    global dict_
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
            dict_.get(str(message.from_user.id))['city'] = message.text
            print(dict_)
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
@threading_func
def get_amount(message):
    """
    Определяет количество отелей по которым необходимо собрать информацию
    """
    global dict_
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
            dict_.get(str(message.from_user.id))['city'] = message.text
            print(dict_)
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
@threading_func
def get_photo(message):
    """
    Определяет необходимость загрузки фото
    """
    global dict_
    if re.match(r'\d{4}-[0-1][0-9]-[0-3][0-9], \d{4}-[0-1][0-9]-[0-3][0-9]', message.text):
        dict_.get(str(message.from_user.id))['check_in'] = message.text.split(', ')[0]
        dict_.get(str(message.from_user.id))['check_out'] = message.text.split(', ')[1]
        print(dict_)
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
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='Yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='No')
    keyboard.add(key_no)
    info_all = 'Ищем {amount} отелей в городе {city} с {photo_amount} фото'.format(
        amount=dict_.get(str(message.from_user.id))['amount'],
        city=dict_.get(str(message.from_user.id))['city'],
        photo_amount=dict_.get(str(message.from_user.id))['photo_amount']
    )
    bot.send_message(message.from_user.id, text=info_all, reply_markup=keyboard)


def restart(message):
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Для нового поиска нажми "Начать поиск"'
    keyboard.row(
        types.InlineKeyboardButton(text='Начать поиск', callback_data='start_search')
    )
    bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
@threading_func
def callback_worker(call):
    """
    Обработка запроса.
    """
    global dict_
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
            if call.from_user.id == dict_.get(str(call.from_user.id)):
                dict_[str(call.from_user.id)]['command'] = 'lowprice'
            print(dict_)
            get_city(call.message)

        elif call.data == 'start_search':
            bot.answer_callback_query(call.id)
            start_key_board(call.message)

        elif call.data == "/highprice":
            bot.answer_callback_query(call.id)
            if call.from_user.id == dict_.get(str(call.from_user.id)):
                dict_[str(call.from_user.id)]['command'] = 'highprice'
            print(dict_)
            get_city(call.message)

        elif call.data == "/bestdeal":
            bot.answer_callback_query(call.id)
            if call.from_user.id == dict_.get(str(call.from_user.id)):
                dict_[str(call.from_user.id)]['command'] = 'bestdeal'
            print(dict_)
            get_city(call.message)

        elif call.data in ['London', 'New York', 'Paris']:
            bot.answer_callback_query(call.id)
            dict_[str(call.from_user.id)]['city'] = call.data
            print(dict_)
            if dict_.get(str(call.from_user.id))['command'] == 'bestdeal':
                get_range_price(call)
            else:
                get_amount(call)

        elif call.data == 'my_city':
            bot.answer_callback_query(call.id)
            if dict_.get(str(call.from_user.id))['command'] == 'bestdeal':
                bot.register_next_step_handler(call.message, get_range_price)
            else:
                bot.register_next_step_handler(call.message, get_amount)

        elif re.search(r'\d{,3}, \d{,3}', call.data):
            bot.answer_callback_query(call.id)
            dict_.get(str(call.from_user.id))['range_price'] = call.data.split(', ')
            print(dict_)
            get_range_distance(call.message)

        elif call.data.startswith('dist_'):
            bot.answer_callback_query(call.id)
            dict_.get(str(call.from_user.id))['range_distance'] = call.data.lstrip('dist_')
            print(dict_)
            get_amount(call)

        elif call.data.startswith('amount_'):
            bot.answer_callback_query(call.id)
            dict_.get(str(call.from_user.id))['amount'] = call.data.lstrip('amount_')
            print(dict_)
            get_date(call.message)

        elif call.data.startswith('photo_'):
            bot.answer_callback_query(call.id)
            dict_.get(str(call.from_user.id))['photo_amount'] = call.data.lstrip('photo_')
            print(dict_)
            get_confirmation(call)

        elif call.data == "Yes":
            bot.answer_callback_query(call.id)
            res = parsing(dict_.get(str(call.from_user.id)))
            amount = len(res)
            print(res)
            if res == []:
                bot.send_message(call.message.chat.id, 'Я не смог ничего найти')
                restart(call.message)
            else:
                if '$' in res[0][4]:
                    bot.send_message(call.message.chat.id, 'Я смог найти {} из {} отелей'.format(
                        amount,
                        dict_[str(call.from_user.id)].get('amount')
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
            dict_[str(call.from_user.id)]['photo_amount'] = 0
            get_confirmation(call)


if __name__ == '__main__':
    bot.polling(none_stop=True)
