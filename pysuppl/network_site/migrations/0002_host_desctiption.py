# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='desctiption',
            field=models.TextField(default='OK'),
            preserve_default=False,
        ),
    ]
