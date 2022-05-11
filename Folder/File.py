import telebot
from telebot import types
from Parser import parsing
import settings
import re


bot = telebot.TeleBot(settings.KEY)
info = dict()


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     'Привет, {name}!\nНе знаешь с чего начать?\nХочешь узнать что я могу?\nНажми кнопку хелп. '
                     'Или выбери другую команду.'.format(
                         name=message.from_user.first_name))

    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Могу найти отели:'
    keyboard.row(
        types.InlineKeyboardButton(text='Дешовые', callback_data='/lowprice'),
        types.InlineKeyboardButton(text='Дорогие', callback_data='/highprice'),
        types.InlineKeyboardButton(text='Для вас', callback_data='/bestdeal')
    )
    keyboard.row(
        types.InlineKeyboardButton(text='help', callback_data='/help'),
        types.InlineKeyboardButton(text='history', callback_data='/history'),
    )
    bot.send_message(message.from_user.id, text=key_message, reply_markup=keyboard)

# @bot.message_handler(content_types=['text'])
# def get_message(message):


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     'Здесь текст описания бота')

    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Не забудь отправить коммент автору.'
    key_author = types.InlineKeyboardButton(text='Написать автору', url='telegram.me/AuthorTB')
    keyboard.add(key_author)
    bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)


# @bot.message_handler(commands=['lowprice'])
# def lowprice(message):
#     '''
#     Подбирает самые дешовые отели.
#     '''
#     # info['command'] = 'lowprice'
#     # get_city(message)


# @bot.message_handler(commands=['highprice'])
# def highprice(message):
#     '''
#     Подбирает самые дорогие отели.
#     '''
#     info['command'] = 'highprice'
#     bot.send_message(message.chat.id, 'Давайте начнем')
#     get_city(message)


# @bot.message_handler(commands=['bestdeal'])
# def bestdeal(message):
#     '''
#     Подбирает отели c лучшими совпадениями.
#     '''
#     info['command'] = 'bestdeal'
#     bot.send_message(message.chat.id, 'Давайте начнем')
#     get_city(message)


@bot.message_handler(commands=['history'])
def history(message):
    '''
    История запросов.
    '''
    with open('log.txt', 'r') as log_file:
        history = log_file.readlines()
    bot.send_message(message.chat.id, '{}'.format(history))


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
    # if not message.text.isascii():
    #     bot.send_message(message.chat.id, 'В названии города используйте только латинские буквы')
    #     get_city(message)
    # else:
    #     if message.text.isalpha():
    #         info['city'] = message.text
    #     bot.send_message(message.chat.id, 'Укажите диапазон цен за ночь, через запятую')
    #     print(info)
    #     bot.register_next_step_handler(message, get_range_distance)
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Укажите стоимость номера за ночь'
    keyboard.row(
        types.InlineKeyboardButton(text='До 25', callback_data='0, 25'),
        types.InlineKeyboardButton(text='От 25 до 75', callback_data='25, 75'),
        types.InlineKeyboardButton(text='От 75 до 150', callback_data='75, 150'),
        # types.InlineKeyboardButton(text='От 150 до 250', callback_data='150, 250'),
        # types.InlineKeyboardButton(text='От 250 до 500', callback_data='250, 500')
    )
    keyboard.row(
        types.InlineKeyboardButton(text='От 150 до 250', callback_data='150, 250'),
        types.InlineKeyboardButton(text='От 250 до 500', callback_data='250, 500')
    )
    bot.send_message(message.message.chat.id, text=key_message, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_range_distance(message):
    # if not re.search(r'\d{2,}, \d{2,}', message.text):
    #     bot.send_message(message.chat.id, 'Давай-ка еще раз. Число. Запятая. Пробел. Число.')
    #     get_range_price(message)
    # else:
    #     info['range_price'] = message.text.split(', ')
    #     bot.send_message(message.chat.id, 'Укажите расстояние от центра в милях. Целое число.')
    #     print(info)
    #     bot.register_next_step_handler(message, get_amount)
    keyboard = types.InlineKeyboardMarkup()
    key_message = 'Укажите расстояние от центра в милях.'
    keyboard.row(
        types.InlineKeyboardButton(text='1', callback_data='1'),
        types.InlineKeyboardButton(text='2', callback_data='2'),
        types.InlineKeyboardButton(text='3', callback_data='3'),
        types.InlineKeyboardButton(text='4', callback_data='4'),
        types.InlineKeyboardButton(text='5', callback_data='5')
    )
    bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_amount(message):
    """
    Определяет количество отелей оп которым необходимо собрать информацию
    """
    try:
        if message.text.isascii():
            info['city'] = message.text

        else:
            bot.send_message(message.chat.id, 'В названии города используйте только латинские буквы')
            get_city(message)
    except:
        pass
    finally:
        keyboard = types.InlineKeyboardMarkup()
        key_message = 'Укажите кол-во отелей.'
        keyboard.row(
            types.InlineKeyboardButton(text='1', callback_data='amount_1'),
            types.InlineKeyboardButton(text='2', callback_data='amount_2'),
            types.InlineKeyboardButton(text='3', callback_data='amount_3'),
            types.InlineKeyboardButton(text='4', callback_data='amount_4'),
            types.InlineKeyboardButton(text='5', callback_data='amount_5')
        )
        bot.send_message(message.chat.id, text=key_message, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_date(message):
    """
    Определяет период за который необходимо
    """
        bot.send_message(message.chat.id, 'Укажите даты въезда и выезда через запятую в формате гггг-мм-дд')
        bot.register_next_step_handler(message, get_photo)
    else:
        bot.send_message(message.chat.id, 'Используйте цифры, кол-во не должно быть больше 5-ти')
        bot.register_next_step_handler(message, get_date)


@bot.message_handler(content_types=['text'])
def get_photo(message):
    """
    Определяет необходимость загрузки фото
    """
    if re.match(r'\d{4}-[0-1][0-9]-[0-3][0-9], \d{4}-[0-1][0-9]-[0-3][0-9]', message.text):
        info['check_in'] = message.text.split(', ')[0]
        info['check_out'] = message.text.split(', ')[1]
        bot.send_message(message.chat.id, 'Загрузить фото по отелям?')
        bot.register_next_step_handler(message, get_photo_amount)
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
    if not message.text.lower() == 'да':
        get_confirmation(message)
    else:
        bot.send_message(message.chat.id, 'Сколько фото(не больше пяти)?')
        bot.register_next_step_handler(message, get_confirmation)


@bot.message_handler(content_types=['text'])
def get_confirmation(message):
    """
    Проверка запрашиваемых даных.
    """
    if message.text.isdigit():
        info['photo_amount'] = int(message.text)
    elif message.text.lower() == 'нет':
        info['photo_amount'] = 0
    else:
        bot.send_message(message.chat.id, 'Используйте цифры')
        bot.register_next_step_handler(message, get_photo_amount)
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

        elif call.data == "/highprice":
            bot.answer_callback_query(call.id)
            info['command'] = 'highprice'
            get_city(call.message)

        elif call.data == "/bestdeal":
            bot.answer_callback_query(call.id)
            info['command'] = 'bestdeal'
            get_city(call.message)

        elif call.data in ['London', 'New York', 'Pris']:
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

        elif call.data in range(1, 6):
            info['range_distance'] = float(call.data)
            get_amount(call.message)

        elif call.data.startswith('amount_'):
            info['amount'] = call.data.lstrip('amount_')
            print(info)
            get_date(call.message)

        elif call.data == "Yes":
            bot.answer_callback_query(call.id)
            res = parsing(info)
            amount = len(res)
            print(res)
            if res == []:
                bot.send_message(call.message.chat.id, 'Я не смог ничего найти')
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
                                photos=res[i][5:]
                            ))
                else:
                    for i in range(amount):
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
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, 'Начнем сначала')
            welcome(call.message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
