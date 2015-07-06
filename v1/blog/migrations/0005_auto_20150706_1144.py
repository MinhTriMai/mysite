# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150706_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False),
        ),
    ]
