# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_auto_20141201_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='username',
            new_name='user',
        ),
    ]
