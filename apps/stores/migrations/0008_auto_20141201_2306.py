# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_auto_20141201_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statustype',
            old_name='status_name',
            new_name='name',
        ),
    ]
