# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-01 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_simple_cms', '0005_set_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuup.Shop', verbose_name='shop'),
        ),
    ]