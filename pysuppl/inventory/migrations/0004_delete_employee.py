# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_computer_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
