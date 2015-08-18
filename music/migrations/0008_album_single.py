# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_article_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=25)),
                ('timing', models.TimeField()),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=25)),
                ('link', models.FileField(upload_to='')),
            ],
        ),
    ]
