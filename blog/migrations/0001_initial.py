# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNotis',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('main', models.ForeignKey(to='youtube.Main')),
            ],
        ),
    ]
