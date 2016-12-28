# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ideograph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('pinyin', models.CharField(max_length=20, null=True)),
                ('pinyin_no_accent', models.CharField(max_length=20, null=True)),
                ('image', models.CharField(max_length=50, null=True)),
                ('audio', models.CharField(max_length=50, null=True)),
                ('meaning', models.CharField(max_length=100)),
                ('invented_meaning', models.BooleanField(default=False)),
                ('tone', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=50, null=True)),
                ('position', models.IntegerField()),
                ('ideograph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinese.Ideograph')),
            ],
        ),
    ]