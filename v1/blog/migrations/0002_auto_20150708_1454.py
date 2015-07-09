# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='file',
            field=models.FileField(upload_to=b'user_upload/files/', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to=b'user_upload/images/', blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', blank=True),
        ),
    ]
