# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_album_single'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='timing',
            field=models.TextField(max_length=8),
        ),
    ]
