# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-02-04 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skar', '0007_testimonials_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Name'),
        ),
    ]
