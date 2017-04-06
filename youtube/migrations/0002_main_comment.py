# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
