from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class News(models.Model):
    author = models.ForeignKey(
        'Profile',
        verbose_name='Автор',
        default=None, null=True,
        on_delete=models.CASCADE,
        related_name='author',
        blank=True
    )
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    content = models.CharField(verbose_name='Содержание', max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    interest = models.BooleanField(verbose_name='Активность', default=False)


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        default=None, null=True,
        on_delete=models.CASCADE,
        related_name='user',
        blank=True
    )
    anonusername = models.CharField(verbose_name='Имя пользователя', max_length=100)
    comment = models.TextField(verbose_name='Комментарий', max_length=1000)
    news = models.ForeignKey(
        'News',
        verbose_name='Новость',
        default=None, null=True,
        on_delete=models.CASCADE,
        related_name='news',
        blank=True
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Юзер', null=True, default=None)
    phone_number = models.CharField(max_length=36, blank=True, verbose_name='Номер телефона')
    city = models.CharField(max_length=36, blank=True, verbose_name='Город')
    verification = models.BooleanField(default=False, verbose_name='Верифицырован')
    publish_count = models.IntegerField(blank=True, default=0, null=False)

    def __str__(self):
        return self.user.username
