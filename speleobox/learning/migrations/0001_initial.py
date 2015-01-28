# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=255)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('value', models.CharField(max_length=255)),
                ('dimensions', models.CharField(max_length=15)),
                ('entrance', models.CharField(max_length=15)),
                ('exit', models.CharField(max_length=15)),
                ('is_dead_end', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='node',
            index_together=set([('value', 'entrance', 'exit', 'dimensions', 'is_dead_end')]),
        ),
    ]
