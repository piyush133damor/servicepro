# Generated by Django 3.0.3 on 2020-02-24 11:59

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0008_auto_20200222_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='lattitude',
            field=models.DecimalField(decimal_places=10, default=Decimal('0'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='shop',
            name='longitude',
            field=models.DecimalField(decimal_places=10, default=Decimal('0'), max_digits=20),
        ),
    ]
