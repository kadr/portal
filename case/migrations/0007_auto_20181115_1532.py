# Generated by Django 2.1.3 on 2018-11-15 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0006_auto_20181115_1112'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='case',
        #     name='created_at',
        # ),
        migrations.AlterField(
            model_name='case',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 15, 32, 36, 727589), verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='case',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 15, 32, 36, 727568), verbose_name='Дата старта'),
        ),
    ]