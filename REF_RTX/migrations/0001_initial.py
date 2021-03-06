# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-28 01:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100, unique=True)),
                ('doctor_email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='followup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('PRE-RTX', 'PRE-RTX'), ('RTX-3 Monthes', 'RTX-3M'), ('RTX-6 Monthes', 'RTX-6M'), ('RTX-9 Monthes', 'RTX-9M'), ('RTX-12 Monthes', 'RTX-12M'), ('RTX-15 Monthes', 'RTX-15M'), ('RTX-18 Monthes', 'RTX-18M'), ('RTX-21 Monthes', 'RTX-21M'), ('RTX-24 Monthes', 'RTX-24M'), ('RTX-27 Monthes', 'RTX-27M'), ('RTX-30 Monthes', 'RTX-30M')], max_length=50, null=True)),
                ('followup_date', models.DateField(blank=True, null=True)),
                ('cd19_abs_count', models.FloatField(blank=True, null=True)),
                ('upcr', models.FloatField(blank=True, null=True)),
                ('serum_albumin', models.FloatField(blank=True, null=True)),
                ('creatinine', models.FloatField(blank=True, null=True)),
                ('CRP', models.FloatField(blank=True, null=True)),
                ('ESR', models.FloatField(blank=True, null=True)),
                ('ANCA_titre', models.FloatField(blank=True, null=True)),
                ('PR3_titre', models.FloatField(blank=True, null=True)),
                ('MPO_titre', models.FloatField(blank=True, null=True)),
                ('urine_rbc', models.CharField(blank=True, choices=[('< 10', '< 10'), ('10 - 100', '10 - 100'), ('> 100', '> 100')], max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100, unique=True, verbose_name='Hospital Name')),
                ('city', models.CharField(choices=[('Perth', 'Perth'), ('Hobart', 'Hobart'), ('Melbourne', 'Melbourne'), ('Darwin', 'Darwin'), ('Sydney', 'Sydney')], max_length=15)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UMRN', models.CharField(max_length=10, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('DOB', models.DateField()),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], max_length=20, null=True)),
                ('date_of_diagnosis', models.DateField()),
                ('Diagnosis_type', models.CharField(blank=True, choices=[('Lupus Nephritis', 'Lupus Nephritis'), ('Vasculitis', 'Vasculitis'), ('Nephrotic Syndrome', 'Nephrotic Syndrome'), ('MPGN', 'MPGN')], default='Nephrotic Syndrome', max_length=200, null=True)),
                ('Diagnosis_subtype', models.CharField(blank=True, choices=[('Lupus Nephritis', (('Class3', 'Class3'), ('Class4', 'Class4'), ('Class5', 'Class5'), ('Class3 and Class5', 'Class3 and Class5'), ('Class4 and Class5', 'Class4 and Class5'))), ('Vasculitis', (('ANCA MPO', 'ANCA MPO'), ('ANCA PR3', 'ANCA PR3'), ('ANCA -VE', 'ANCA -VE'), ('Other', 'Other'))), ('Nephrotic Syndrome', (('Minimal Change', 'Minimal Change'), ('FSGS', 'FSGS'), ('Membranous', 'Membranous')))], max_length=200, null=True)),
                ('Previous_treatment', multiselectfield.db.fields.MultiSelectField(choices=[('Prednisolone', 'Prednisolone'), ('Tacrolimus', 'Tacrolimus'), ('Mycophenolate', 'Mycophenolate'), ('Cyclosporin', 'Cyclosporin'), ('Cyclophosphamide', 'Cyclophosphamide'), ('Azathioprine', 'Azathioprine'), ('Methotrexate', 'Methotrexate'), ('Rituximab', 'Rituximab'), ('Other', 'Other')], max_length=108)),
                ('prev_other_comment', models.CharField(blank=True, max_length=50, null=True)),
                ('pre_rtx_date', models.DateField()),
                ('pre_rtx_comment', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Patient', to='REF_RTX.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='rtx_infusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_infusion', models.DateField(blank=True, null=True)),
                ('no_of_infusion', models.IntegerField(blank=True, null=True)),
                ('dose_in_mg', models.IntegerField(blank=True, null=True)),
                ('concomitant_immunosuppression', multiselectfield.db.fields.MultiSelectField(choices=[('Prednisolone', 'Prednisolone'), ('Tacrolimus', 'Tacrolimus'), ('Mycophenolate', 'Mycophenolate'), ('Cyclosporin', 'Cyclosporin'), ('Cyclophosphamide', 'Cyclophosphamide'), ('Azathioprine', 'Azathioprine'), ('Methotrexate', 'Methotrexate'), ('Rituximab', 'Rituximab'), ('Other', 'Other')], max_length=108)),
                ('schedule_followup_date', models.DateField(blank=True, null=True)),
                ('complication', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='infusion', to='REF_RTX.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='followup',
            name='infusion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rtx_infusion', to='REF_RTX.rtx_infusion'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to='REF_RTX.Hospital'),
        ),
    ]
