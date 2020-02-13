# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-02-04 06:22
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('skar', '0004_auto_20200203_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homebanner',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='static/uploads/%Y/%m/%d'),
        ),
    ]
