# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-24 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0004_auto_20170323_0829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloger',
            options={'verbose_name': 'Блогер', 'verbose_name_plural': 'Блогеры'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='bloger',
            name='is_favorites',
            field=models.BooleanField(default=False, help_text='для избранного !', verbose_name='Избранное'),
        ),
        migrations.AlterField(
            model_name='category',
            name='sort',
            field=models.SmallIntegerField(blank=True, default=100, null=True, verbose_name='Сортировка'),
        ),
    ]
