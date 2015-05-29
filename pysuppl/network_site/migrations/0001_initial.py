# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import network_site.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ip_addr', models.CharField(max_length=100, unique=True, verbose_name='IP-Addr')),
                ('macaddr', models.CharField(max_length=30, validators=[network_site.models.validate_macaddr], unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ipnet', models.CharField(max_length=100, validators=[network_site.models.validate_network], unique=True, verbose_name='IP-Network')),
                ('is_root', models.BooleanField()),
                ('desctiption', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='ip_net',
            field=models.ForeignKey(to='network_site.Network'),
        ),
    ]
