# Generated by Django 2.2 on 2022-05-03 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20220503_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='publish_count',
        ),
    ]
