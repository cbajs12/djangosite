# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=50, null=True)),
                ('comment', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
