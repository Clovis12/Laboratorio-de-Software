# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-20 12:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20170920_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='description email', max_length=254, validators=[django.core.validators.EmailValidator(message='Ingresa un email valido')]),
        ),
    ]
