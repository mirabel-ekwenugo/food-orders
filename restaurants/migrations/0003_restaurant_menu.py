# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='menu',
            field=models.ManyToManyField(to='restaurants.MenuItem'),
        ),
    ]
