# Generated by Django 3.0.6 on 2020-06-23 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200623_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsupdate',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='newsupdate',
            name='news_head',
            field=models.CharField(max_length=27),
        ),
    ]
