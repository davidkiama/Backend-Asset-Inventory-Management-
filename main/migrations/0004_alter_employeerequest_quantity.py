# Generated by Django 4.0.4 on 2022-04-26 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_urgenty_employeerequest_urgency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeerequest',
            name='quantity',
            field=models.CharField(max_length=50),
        ),
    ]