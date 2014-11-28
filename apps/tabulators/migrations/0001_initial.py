# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabulator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tab_zone', models.CharField(max_length=255)),
                ('min_price', models.IntegerField()),
                ('max_price', models.IntegerField()),
                ('media_price', models.IntegerField()),
                ('suggested_price', models.IntegerField(blank=True)),
                ('town', models.ForeignKey(to='core.Town')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
