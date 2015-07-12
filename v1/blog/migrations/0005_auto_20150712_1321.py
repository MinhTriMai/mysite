# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150708_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='hiden',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='blogfile',
            name='file',
            field=models.FileField(upload_to='static/user_upload/files/'),
        ),
        migrations.AlterField(
            model_name='blogimage',
            name='image',
            field=models.ImageField(upload_to='static/user_upload/images/'),
        ),
    ]
