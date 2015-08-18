# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20150813_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
