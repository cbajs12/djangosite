# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='comment',
            field=models.TextField(default=None, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(default=None, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
            preserve_default=True,
        ),
    ]
