# Generated by Django 4.1.3 on 2022-12-15 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_myuser_updated_at_profile_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cert',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contact_no',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id_num',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='person_incharge',
        ),
        migrations.AddField(
            model_name='profile',
            name='id_no',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='身分證字號'),
        ),
        migrations.AddField(
            model_name='profile',
            name='passport_no',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='護照號碼'),
        ),
        migrations.AddField(
            model_name='profile',
            name='residential_no',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='市話'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='姓名'),
        ),
    ]
