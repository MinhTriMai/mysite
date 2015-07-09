# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150708_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'user_upload/files/')),
            ],
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'user_upload/images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='file',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='files',
            field=models.ManyToManyField(to='blog.BlogFile', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ManyToManyField(to='blog.BlogImage', blank=True),
        ),
    ]
