# Generated by Django 4.1.3 on 2022-11-28 15:58

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_address_alter_profile_cert_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 28, 15, 58, 1, 923371)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 28, 15, 58, 9, 117716)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
