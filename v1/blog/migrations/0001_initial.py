# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('date', models.DateField(db_index=True, auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='blog',
            name='topic',
            field=models.ForeignKey(to='blog.Topic'),
        ),
    ]
