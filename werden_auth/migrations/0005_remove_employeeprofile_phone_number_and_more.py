# Generated by Django 4.0.4 on 2022-04-28 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('werden_auth', '0004_managerprofile_employeeprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeprofile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='managerprofile',
            name='phone_number',
        ),
    ]