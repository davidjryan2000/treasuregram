# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treasure',
            name='img_url',
        ),
        migrations.AddField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='treasure_images'),
        ),
    ]
