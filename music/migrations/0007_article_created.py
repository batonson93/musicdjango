# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='Aug. 14, 2015, 5:54 p.m.'),
            preserve_default=False,
        ),
    ]
