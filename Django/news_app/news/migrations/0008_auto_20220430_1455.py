# Generated by Django 2.2 on 2022-04-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20220430_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='verification',
            field=models.BooleanField(default=False, null=True, verbose_name='Верифицырован'),
        ),
    ]