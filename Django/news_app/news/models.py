from django.db import models
from news_app.forms import AuthForm


# Create your models here.
class Auth(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    content = models.CharField(verbose_name='Содержание', max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    interest = models.BooleanField(verbose_name='Активность', default=False)


class Comment(models.Model):
    user_name = models.CharField(verbose_name='Имя пользователя', max_length=100)
    comment = models.TextField(verbose_name='Комментарий', max_length=1000)
    news = models.ForeignKey(
        'News',
        verbose_name='Новость',
        default=None, null=True,
        on_delete=models.CASCADE,
        related_name='news'
    )
    user = models.ForeignKey(
        'AuthForm',
        verbose_name='Пользователь',
        default=None, null=True,
        on_delete=models.CASCADE,
        related_name='user'
    )

