# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20150529_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='role_id',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
