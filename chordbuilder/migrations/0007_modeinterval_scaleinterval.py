# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chordbuilder', '0006_auto_20160301_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModeInterval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('interval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chordbuilder.Interval')),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chordbuilder.Mode')),
            ],
        ),
        migrations.CreateModel(
            name='ScaleInterval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('interval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chordbuilder.Interval')),
                ('scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chordbuilder.Scale')),
            ],
        ),
    ]