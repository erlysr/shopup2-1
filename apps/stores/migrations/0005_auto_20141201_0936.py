# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20141201_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='status',
            field=models.ForeignKey(blank=True, to='stores.StatusType', null=True),
            preserve_default=True,
        ),
    ]
