# Generated by Django 2.2.1 on 2019-07-18 21:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0025_auto_20190718_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 21, 16, 23, 321312, tzinfo=utc)),
        ),
    ]
