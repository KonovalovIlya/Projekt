from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    content = models.CharField(verbose_name='Содержание', max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    interest = models.BooleanField(verbose_name='Активность')


class Comment(models.Model):
    user_name = models.CharField(verbose_name='Имя пользователя', max_length=100)
    comment = models.TextField(verbose_name='Комментарий', max_length=1000)
    news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE, related_name='news')

