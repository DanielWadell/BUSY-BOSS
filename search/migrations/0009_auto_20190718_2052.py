# Generated by Django 2.2.1 on 2019-07-18 20:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20190718_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 20, 52, 58, 203288, tzinfo=utc)),
        ),
    ]
