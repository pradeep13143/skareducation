# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-02-11 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skar', '0008_testimonials_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id_proof_type',
            field=models.CharField(choices=[('Aadhar', 'Aadhar'), ('Driving Licence', 'Driving Licence'), ('Voter ID', 'Voter ID'), ('Pancard', 'Pancard'), ('Passport', 'Passport')], max_length=200, verbose_name='Type of ID proof'),
        ),
    ]
