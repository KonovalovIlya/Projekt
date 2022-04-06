from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, verbouse_name='Заголовок')
    description = models.TextField(verbouse_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)


class User(models.Model):
    name = models.CharField(max_length=100, verbouse_name='Имя пользователя')
    email = models.CharField(max_length=100, verbouse_name='Электронный адрес')
    phone_number = models.CharField(max_length=100, verbouse_name='Номер телефона')
