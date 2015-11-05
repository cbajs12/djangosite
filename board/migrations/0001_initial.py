# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boards',
            fields=[
                ('board_id', models.AutoField(serialize=False, primary_key=True)),
                ('board_pid', models.IntegerField(default=0)),
                ('user_id', models.EmailField(max_length=75, null=True)),
                ('user_name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=50)),
                ('contents', models.TextField()),
                ('hits', models.IntegerField()),
                ('reg_date', models.DateField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
