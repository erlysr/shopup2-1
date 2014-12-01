# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20141201_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.ForeignKey(blank=True, to='core.Address', null=True),
            preserve_default=True,
        ),
    ]
