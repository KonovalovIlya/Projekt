# Generated by Django 2.2 on 2022-05-03 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20220503_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='publish_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Юзер'),
        ),
    ]
