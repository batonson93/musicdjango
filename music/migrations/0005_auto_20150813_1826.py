# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20150813_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(max_length=40),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
