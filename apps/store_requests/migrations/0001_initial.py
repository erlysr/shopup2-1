# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_type', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoreRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_code', models.CharField(max_length=6)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('rent_price', models.FloatField(default=0, null=True, blank=True)),
                ('start_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('rent_type', models.ForeignKey(to='store_requests.RentType')),
                ('status_req', models.ForeignKey(to='stores.StatusType')),
                ('store', models.ForeignKey(to='stores.Store')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
