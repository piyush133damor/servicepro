# Generated by Django 3.0.3 on 2020-07-16 02:39

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0014_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shop',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 16, 8, 9, 51, 206625)),
        ),
        migrations.AlterField(
            model_name='shop',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
    ]
