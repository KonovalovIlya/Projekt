# Generated by Django 2.2 on 2022-05-03 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20220503_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='news.Profile', verbose_name='Автор'),
        ),
    ]
