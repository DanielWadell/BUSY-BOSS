# Generated by Django 2.2.1 on 2019-07-18 21:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('busyapp', '0007_auto_20190718_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 21, 2, 54, 558462, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 21, 2, 54, 557583, tzinfo=utc)),
        ),
    ]
