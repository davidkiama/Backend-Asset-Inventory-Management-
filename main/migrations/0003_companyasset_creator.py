# Generated by Django 4.0.4 on 2022-05-03 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_asset_companyasset'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyasset',
            name='creator',
            field=models.CharField(default='manager', max_length=50),
        ),
    ]