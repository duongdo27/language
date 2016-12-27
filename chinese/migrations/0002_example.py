# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 04:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chinese', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('word', models.CharField(max_length=50, null=True)),
                ('word_meaning', models.CharField(max_length=100, null=True)),
                ('word_pinyin', models.CharField(max_length=100, null=True)),
                ('word_audio', models.CharField(max_length=50, null=True)),
                ('phrase', models.CharField(max_length=100, null=True)),
                ('phrase_meaning', models.CharField(max_length=200, null=True)),
                ('phrase_pinyin', models.CharField(max_length=200, null=True)),
                ('phrase_audio', models.CharField(max_length=50, null=True)),
                ('ideograph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chinese.Ideograph')),
            ],
        ),
    ]
