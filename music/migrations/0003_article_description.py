# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
