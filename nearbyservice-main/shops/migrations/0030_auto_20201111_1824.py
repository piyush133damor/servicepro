# Generated by Django 3.1 on 2020-11-11 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0029_auto_20201105_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.CharField(default=' ', max_length=300),
        ),
        migrations.AlterField(
            model_name='shop',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 11, 18, 24, 39, 35661)),
        ),
    ]
