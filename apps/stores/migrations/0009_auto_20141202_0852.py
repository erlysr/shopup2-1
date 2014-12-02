# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0008_auto_20141201_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='image1',
            new_name='logo',
        ),
    ]
