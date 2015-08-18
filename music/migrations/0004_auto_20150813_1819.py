# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(max_length=20),
        ),
    ]
