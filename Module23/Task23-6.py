# Реализуйте программу — чат, в котором могут участвовать сразу несколько человек, то есть программа может работать
# одновременно для нескольких пользователей. При запуске запрашивается имя пользователя. После этого он выбирает одно
# из действий:
#
# Посмотреть текущий текст чата.
# Отправить сообщение (затем вводит сообщение).
# Действия запрашиваются бесконечно.
import os


user_name = input('Введите ваше имя: ')
# with open('chat.txt', 'a') as chat:
while True:
    print('1. Посмотреть текущий текст чата.\n2. Отправить сообщение.')
    command = int(input())
    if command == 1:
            try:
                with open(r'\\TOPLOG_8_KONOVA\Users\Топлог\PycharmProjects\SkillBox\Projekt\Module23\chat.txt', 'r') as chat:
                    for string in chat:
                        print(string)
            except FileNotFoundError:
                print('V chate net texta')
    elif command == 2:
        with open('chat.txt', 'a') as chat:
            chat.write('{user}: {text}\n'.format(
                user= user_name,
                text= input()
            ))
