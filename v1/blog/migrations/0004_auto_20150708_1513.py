# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150708_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogfile',
            name='file',
            field=models.FileField(upload_to=b'static/user_upload/files/'),
        ),
        migrations.AlterField(
            model_name='blogimage',
            name='image',
            field=models.ImageField(upload_to=b'static/user_upload/images/'),
        ),
    ]
