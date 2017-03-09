# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-09 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-title'], 'verbose_name': 'Книгу', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]