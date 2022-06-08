# Generated by Django 2.2 on 2022-04-22 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Новость', to='news.News'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]