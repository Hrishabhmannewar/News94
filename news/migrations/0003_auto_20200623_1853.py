# Generated by Django 3.0.6 on 2020-06-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsupdate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsupdate',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='newsupdate',
            name='news_head',
            field=models.CharField(max_length=80),
        ),
    ]
