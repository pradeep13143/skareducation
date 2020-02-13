# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-02-04 08:51
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('skar', '0006_whychooseus_whychooseustopics'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='static/uploads/%Y/%m/%d'),
        ),
    ]
