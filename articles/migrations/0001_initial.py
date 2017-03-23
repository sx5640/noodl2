# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField(max_length=500)),
                ('image_url', models.URLField(max_length=500)),
                ('author', models.CharField(max_length=200)),
                ('publication_time', models.DateTimeField()),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sources.Source')),
            ],
        ),
    ]
