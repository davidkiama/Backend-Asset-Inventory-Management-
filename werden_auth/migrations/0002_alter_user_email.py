# Generated by Django 4.0.4 on 2022-05-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werden_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]