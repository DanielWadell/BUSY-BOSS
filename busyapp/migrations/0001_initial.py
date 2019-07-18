# Generated by Django 2.2.1 on 2019-07-18 21:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_username', models.CharField(max_length=264, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='media/profile_pics')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userinfos', to='busyapp.Company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264, unique=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='post_images')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 7, 18, 21, 0, 46, 249293, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='busyapp.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=264)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 7, 18, 21, 0, 46, 249837, tzinfo=utc))),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='busyapp.Post')),
            ],
        ),
    ]
