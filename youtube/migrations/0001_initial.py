# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloger',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Название', max_length=200)),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('img', models.FileField(blank=True, verbose_name='Аватарка', upload_to='bloger/', null=True)),
                ('is_favorites', models.BooleanField(default=False, help_text='для избранного !', verbose_name='Избранное')),
            ],
            options={
                'verbose_name': 'Блогер',
                'verbose_name_plural': 'Блогеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Название', max_length=200)),
                ('sort', models.SmallIntegerField(blank=True, default=100, verbose_name='Сортировка', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='Активность')),
                ('img', models.FileField(blank=True, verbose_name='Картинка', upload_to='category/', null=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True, blank=True, null=True)),
                ('point', models.CharField(null=True, blank=True, default='SO', max_length=100, choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')])),
                ('date_create', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bloger',
            name='category',
            field=models.ForeignKey(default=1, to='youtube.Category', verbose_name='Катагория'),
        ),
    ]
