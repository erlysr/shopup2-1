# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20141201_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='contact',
            field=models.ForeignKey(blank=True, to='stores.Contact', null=True),
            preserve_default=True,
        ),
    ]
