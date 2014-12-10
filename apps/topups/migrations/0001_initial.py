# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topup_name', models.CharField(max_length=255)),
                ('image1', models.ImageField(upload_to=b'topups')),
                ('image2', models.ImageField(upload_to=b'topups', blank=True)),
                ('image3', models.ImageField(upload_to=b'topups', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
