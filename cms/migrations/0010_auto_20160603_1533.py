# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_auto_20160602_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_guidance',
            field=models.CharField(default='', max_length=40, verbose_name='文章导读'),
        ),
        migrations.AlterField(
            model_name='article',
            name='allow_comment',
            field=models.CharField(choices=[('0', '是'), ('1', '否')], default='0', max_length=1, verbose_name='是否容许评论'),
        ),
        migrations.AlterField(
            model_name='article',
            name='check',
            field=models.CharField(choices=[('0', '未审核'), ('1', '审核通过'), ('2', '审核未通过')], default='0', max_length=1, verbose_name='审核状态'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='channel_name',
            field=models.CharField(max_length=10, unique=True, verbose_name='栏目名称'),
        ),
    ]
