from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    user = models.ForeignKey('User', default=None, null=True, on_delete=models.CASCADE,
                             related_name='advertisements')
    category = models.ForeignKey('Category', default=None, null=True, on_delete=models.CASCADE,
                             related_name='category')

    class Meta():
        db_table = 'advertisements'
        ordering = ['title']

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class AdvertisementForm(models.Model):
#     title = models.CharField(max_length=1000)
#     description = models.CharField(max_length=100)
#     price_title = models.CharField(max_length=100)
