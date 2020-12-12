# Generated by Django 3.0.3 on 2020-02-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0007_shop_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='lattitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='shop',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=20),
        ),
    ]
