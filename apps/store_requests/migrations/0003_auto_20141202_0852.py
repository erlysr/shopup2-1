# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_requests', '0002_auto_20141201_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storerequest',
            options={'verbose_name': 'Petici\xf3n de Tienda', 'verbose_name_plural': 'Peticiones de Tiendas'},
        ),
    ]
