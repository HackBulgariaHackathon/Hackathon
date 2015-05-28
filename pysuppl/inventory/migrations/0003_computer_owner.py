# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0002_auto_20150526_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=datetime.datetime(2015, 5, 28, 9, 45, 16, 872212, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
