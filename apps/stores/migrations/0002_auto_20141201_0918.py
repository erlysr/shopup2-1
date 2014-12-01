# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='others1',
            new_name='mostrador',
        ),
        migrations.RemoveField(
            model_name='store',
            name='others2',
        ),
        migrations.RemoveField(
            model_name='store',
            name='others3',
        ),
        migrations.AlterField(
            model_name='store',
            name='tabulator',
            field=models.ForeignKey(blank=True, to='tabulators.Tabulator', null=True),
            preserve_default=True,
        ),
    ]
