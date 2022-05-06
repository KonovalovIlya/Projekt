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
    info['command'] = 'lowprice'
    bot.send_message(message.chat.id, 'Давайте начнем')
    get_city(message)


@bot.message_handler(commands=['highprice'])
def highprice(message):
    '''
    Подбирает самые дорогие отели.
    '''
    info['command'] = 'highprice'
    bot.send_message(message.chat.id, 'Давайте начнем')
    get_city(message)


@bot.message_handler(commands=['bestdeal'])
def bestdeal(message):
    '''
    Подбирает отели c лучшими совпадениями.
    '''
    info['command'] = 'bestdeal'
    bot.send_message(message.chat.id, 'Давайте начнем')
    get_city(message)


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
    bot.send_message(message.chat.id, 'В каком городе подобрать отель?')
    if info['command'] == 'bestdeal':
        bot.register_next_step_handler(message, get_range_price)
        print(info)
    else:
        bot.register_next_step_handler(message, get_amount)


@bot.message_handler(content_types=['text'])
def get_range_price(message):
    if not message.text.isascii():
        bot.send_message(message.chat.id, 'В названии города используйте только латинские буквы')
        get_city(message)
    else:
        if message.text.isalpha():
            info['city'] = message.text
        bot.send_message(message.chat.id, 'Укажите диапазон цен за ночь, через запятую')
        print(info)
        bot.register_next_step_handler(message, get_range_distance)



@bot.message_handler(content_types=['text'])
def get_range_distance(message):
    # if not message.text.isdigit:
    if not re.search(r'\d{2,}, \d{2,}', message.text):
        bot.send_message(message.chat.id, 'Давай-ка еще раз. Число. Запятая. Пробел. Число.')
        get_range_price(message)
    else:
        info['range_price'] = message.text.split(', ')
        bot.send_message(message.chat.id, 'Укажите расстояние от центра в милях. Целое число.')
        print(info)
        bot.register_next_step_handler(message, get_amount)


@bot.message_handler(content_types=['text'])
def get_amount(message):
    """
    Определяет количество отелей оп которым необходимо собрать информацию
    """
    if info['command'] == 'bestdeal':
        if ',' in message.text or '.' in message.text or not message.text.isdigit:
            bot.send_message(message.chat.id, 'Давай-ка еще раз. Целое. Число.')
            get_range_distance(message)
        else:
            info['range_distance'] = float(message.text)
            bot.send_message(message.chat.id, 'Укажите кол-во отелей (не больше пяти)')
            print(info)
            bot.register_next_step_handler(message, get_date)
    else:
        if message.text.isascii():
            info['city'] = message.text
            bot.send_message(message.chat.id, 'Укажите кол-во отелей (не больше пяти)')
            bot.register_next_step_handler(message, get_date)
        else:
            bot.send_message(message.chat.id, 'В названии города используйте только латинские буквы')
            get_city(message)



@bot.message_handler(content_types=['text'])
def get_date(message):
    """
    Определяет период за который необходимо
    """
    if message.text.isdigit() and int(message.text) <= settings.MAX_HOTELS:
        info['amount'] = message.text
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
    if call.data == "Yes":
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
        bot.send_message(call.message.chat.id, 'Начнем сначала')
        get_city(call.message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
