# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('top_name', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=100)),
                ('url', models.URLField(unique=True)),
                ('topic', models.ForeignKey(to='final_application.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='accessrecord',
            name='name',
            field=models.ForeignKey(to='final_application.Webpage'),
        ),
    ]
