# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network_site', '0006_auto_20150526_1347'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vlans',
            new_name='Vlan',
        ),
    ]
