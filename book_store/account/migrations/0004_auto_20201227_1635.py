# Generated by Django 3.1.1 on 2020-12-27 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20201027_0508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='apartment_number',
        ),
        migrations.RemoveField(
            model_name='account',
            name='city',
        ),
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='zip_code',
        ),
    ]
