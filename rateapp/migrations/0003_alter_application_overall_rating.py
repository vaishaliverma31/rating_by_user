# Generated by Django 3.2.4 on 2021-06-20 08:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateapp', '0002_auto_20210620_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='overall_rating',
            field=models.FloatField(default=0, null=True, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(2)]),
        ),
    ]
