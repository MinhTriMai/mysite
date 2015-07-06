# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150706_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(max_length=500, blank=True),
        ),
    ]
