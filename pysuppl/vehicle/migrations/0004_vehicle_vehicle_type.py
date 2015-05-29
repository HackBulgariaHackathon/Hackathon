# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_auto_20150528_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(max_length=100, default=datetime.datetime(2015, 5, 28, 21, 21, 59, 588419, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
