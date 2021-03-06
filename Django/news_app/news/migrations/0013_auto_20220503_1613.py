# Generated by Django 2.2 on 2022-05-03 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20220503_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='news.Profile', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='publish_count',
            field=models.IntegerField(blank=True, default=0, max_length=1000, null=True),
        ),
    ]
