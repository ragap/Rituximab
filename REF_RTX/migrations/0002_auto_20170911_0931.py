# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-11 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('REF_RTX', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Doctor', to='REF_RTX.Hospital'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='infusion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rtx_infusion', to='REF_RTX.rtx_infusion'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Patient', to='REF_RTX.Doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pre_rtx_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rtx_infusion',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='infusion', to='REF_RTX.Patient'),
        ),
    ]
