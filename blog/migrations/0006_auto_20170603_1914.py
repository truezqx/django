# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_hellspawn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_publish',
            field=models.DateTimeField(verbose_name='发布时间', auto_now_add=True),
        ),
    ]
