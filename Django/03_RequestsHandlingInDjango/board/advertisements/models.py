from django.db import models

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return self.title