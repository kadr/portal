# Generated by Django 2.1.3 on 2018-11-15 07:08
import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_file'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='case',
        #     name='created_at',
        # ),
        migrations.AddField(
            model_name='case',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 10, 9, 6, 299179), verbose_name='Дата окончания'),
        ),
        migrations.AddField(
            model_name='case',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 10, 9, 6, 299179), verbose_name='Дата старта'),
        ),
    ]
