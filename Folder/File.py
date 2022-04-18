import telebot
from telebot import types
from Parser import parsing
import settings


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
    '''
    Город, где будет проводиться поиск.
    '''
    bot.send_message(message.chat.id, 'В каком городе подобрать отель?')
    bot.register_next_step_handler(message, get_city)


@bot.message_handler(content_types=['text'])
def get_city(message):
    info['city'] = message.text
    bot.send_message(message.chat.id, 'Укажите кол-во отелей (не больше пяти)')
    bot.register_next_step_handler(message, get_amount)


@bot.message_handler(content_types=['text'])
def get_amount(message):
    # 2. Количество отелей, которые необходимо вывести в результате(не больше заранее определённого максимума).
    # bot.send_message(message.chat.id, 'Укажите кол-во отелей (не больше пяти)')
    # while int(message.text) > 5:
    #     bot.send_message(message.chat.id, 'Кол-во отелей должно быть не больше пяти)')
    info['amount'] = message.text
    bot.send_message(message.chat.id, 'Укажите даты въезда и выезда через запятую в формате гггг-мм-дд')
    bot.register_next_step_handler(message, get_date)


@bot.message_handler(content_types=['text'])
def get_date(message):
    info['check_in'] = message.text.split(', ')[0]
    info['check_out'] = message.text.split(', ')[1]
    bot.send_message(message.chat.id, 'Загрузить фото по отелям?')
    bot.register_next_step_handler(message, get_foto)


@bot.message_handler(content_types=['text'])
def get_foto(message):
    if message.text == 'Да':
    # 3. Необходимость загрузки и вывода фотографий для каждого отеля(“Да / Нет”)
    # bot.send_message(message.chat.id, 'Загрузить фото по отелям?')
        bot.send_message(message.chat.id, 'Сколько фото(не больше пяти)?')
        bot.register_next_step_handler(message, get_photo_amount)
    else:
        bot.register_next_step_handler(message, get_photo_amount)


@bot.message_handler(content_types=['text'])
def get_photo_amount(message):
    # if message.text == 'Да':
        # bot.send_message(message.chat.id, 'Сколько фото(не больше пяти)?')
    info['photo_amount'] = int(message.text)
        # a.При положительном ответе пользователь также вводит количество необходимых фотографий(не больше заранее
        #         определённого максимума)
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
