import telebot
from telebot import types
from Parser import parsing
import settings
from settings import info
import re


bot = telebot.TeleBot(settings.KEY)

@bot.message_handler(commands=['start'])
def welcome(message):
    '''
    Приветствует пользователя
    '''
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
            'Если нажмешь на кнопку "Дорогие", я подберу самые дорогие отели.\n'\
            'Если нажмешь на кнопку "Для вас", я подберу самые подходящие отели под указанные параметры.\n'\
            'Если нажмешь на кнопку "History", я отправлю тебе файл с ответами на все запросы которые ты мне отправлял.\n'
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
    bot.send_document(message.chat.id, open(r'log.txt', 'rb'))

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
            info['city'] = message.text
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
            info['city'] = message.text
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
    if re.match(r'\d{4}-[0-1][0-9]-[0-3][0-9], \d{4}-[0-1][0-9]-[0-3][0-9]', message.text):
        info['check_in'] = message.text.split(', ')[0]
        info['check_out'] = message.text.split(', ')[1]
        #bot.send_message(message.chat.id, 'Загрузить фото по отелям?')
        #bot.register_next_step_handler(message, get_photo_amount)
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
        amount=info['amount'],
        city=info['city'],
        photo_amount=info['photo_amount']
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
def callback_worker(call):
    """
    Обработка запроса.
    """
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
            info['command'] = 'lowprice'
            get_city(call.message)

        elif call.data == 'start_search':
            start_key_board(call.message)

        elif call.data == "/highprice":
            bot.answer_callback_query(call.id)
            info['command'] = 'highprice'
            get_city(call.message)

        elif call.data == "/bestdeal":
            bot.answer_callback_query(call.id)
            info['command'] = 'bestdeal'
            get_city(call.message)

        elif call.data in ['London', 'New York', 'Paris']:
            info['city'] = call.data
            if info['command'] == 'bestdeal':
                get_range_price(call)
            else:
                get_amount(call)

        elif call.data == 'my_city':
            if info['command'] == 'bestdeal':
                bot.register_next_step_handler(call.message, get_range_price)
            else:
                bot.register_next_step_handler(call.message, get_amount)

        elif re.search(r'\d{,3}, \d{,3}', call.data):
            print('Нашел')
            info['range_price'] = call.data.split(', ')
            get_range_distance(call.message)

        elif call.data.startswith('dist_'):
            info['range_distance'] = call.data.lstrip('dist_')
            print(info)
            get_amount(call)

        elif call.data.startswith('amount_'):
            info['amount'] = call.data.lstrip('amount_')
            print(info)
            get_date(call.message)

        elif call.data.startswith('photo_'):
            info['photo_amount'] = call.data.lstrip('photo_')
            print(info)
            get_confirmation(call)

        elif call.data == "Yes":
            bot.answer_callback_query(call.id)
            res = parsing(info)
            amount = len(res)
            print(res)
            if res == []:
                bot.send_message(call.message.chat.id, 'Я не смог ничего найти')
                bot.send_message(call.message.chat.id, 'Для вызова начальной клавиатуры нажми /start')
            else:
                if '$' in res[0][4]:
                    bot.send_message(call.message.chat.id, 'Я смог найти {} из {} отелей'.format(amount, info.get('amount')))
                    for i in range(amount):
                        bot.send_message(
                            call.message.chat.id, 'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
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
                            call.message.chat.id, 'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
                            'цена за ночь - {price}, {photos}'.format(
                                name=res[i][0],
                                street=res[i][1],
                                distance=res[i][2],
                                price=res[i][3],
                                photos=', '.join(res[i][4:])
                            ))
                    restart(call.message)


        elif call.data == "No":
            bot.send_message(call.message.chat.id, 'Начнем сначала')
            start_key_board(call.message)

        elif call.data == 'yes_p':
          get_photo_amount(call)

        elif call.data == 'no_p':
          info['photo_amount'] = 0
          get_confirmation(call)

if __name__ == '__main__':
    bot.polling(none_stop=True)