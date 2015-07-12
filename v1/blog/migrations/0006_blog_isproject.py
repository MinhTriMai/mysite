# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150712_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='isProject',
            field=models.BooleanField(default=False),
        ),
    ]
