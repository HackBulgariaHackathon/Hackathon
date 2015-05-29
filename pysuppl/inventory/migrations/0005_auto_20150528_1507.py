# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_delete_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='software',
            old_name='comment',
            new_name='description',
        ),
    ]
