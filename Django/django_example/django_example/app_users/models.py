from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)