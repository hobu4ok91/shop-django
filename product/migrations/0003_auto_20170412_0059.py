# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20170411_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='static/media/products_images'),
        ),
    ]
