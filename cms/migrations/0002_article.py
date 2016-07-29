# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 05:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=30, verbose_name='文章标题')),
                ('article_content', models.TextField(verbose_name='内容')),
                ('add_date', models.DateField()),
                ('keys', models.CharField(max_length=50, verbose_name='关键字')),
                ('article_from', models.CharField(max_length=50, verbose_name='文章来源')),
                ('modify_date', models.DateField(auto_now=True, null=True)),
                ('add_user', models.CharField(max_length=15)),
                ('allow_comment', models.CharField(choices=[('0', '是'), ('1', '否')], max_length=1, verbose_name='是否容许评论')),
                ('check', models.CharField(choices=[('0', '未审核'), ('1', '审核通过'), ('2', '审核未通过')], max_length=1, verbose_name='审核状态')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Channel')),
            ],
        ),
    ]
