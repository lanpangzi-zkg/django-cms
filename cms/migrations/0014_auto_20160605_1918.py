# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20160605_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_icon',
            field=models.ImageField(null=True, upload_to='', verbose_name='文章图片'),
        ),
    ]
