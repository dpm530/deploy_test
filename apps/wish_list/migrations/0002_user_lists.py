# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-26 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lists',
            field=models.ManyToManyField(related_name='_user_lists_+', to='wish_list.User'),
        ),
    ]
