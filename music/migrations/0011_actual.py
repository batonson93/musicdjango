# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=50, blank=True)),
                ('image', models.ImageField(upload_to='', blank=True)),
                ('audio', models.FileField(upload_to='', blank=True)),
                ('video', models.URLField(blank=True)),
            ],
        ),
    ]
