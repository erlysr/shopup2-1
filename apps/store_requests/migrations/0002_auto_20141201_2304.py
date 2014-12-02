# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_requests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storerequest',
            old_name='date_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='storerequest',
            old_name='status_req',
            new_name='status_type',
        ),
        migrations.RemoveField(
            model_name='storerequest',
            name='request_code',
        ),
    ]
