# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 00:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bidtype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('bidtypes', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.Channel'),
        ),
    ]