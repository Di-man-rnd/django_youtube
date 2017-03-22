# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-21 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20170321_1035'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('count', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='inc',
            field=models.SmallIntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
