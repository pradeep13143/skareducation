# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-02-03 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skar', '0003_auto_20200203_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcontent',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='skar.StudentCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachercontent',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='skar.TeacherCategory'),
            preserve_default=False,
        ),
    ]
