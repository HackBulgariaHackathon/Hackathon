# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='number',
            field=models.CharField(max_length=6, default=datetime.datetime(2015, 5, 28, 16, 20, 0, 560767, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
