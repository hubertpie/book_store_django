# Generated by Django 3.1.1 on 2020-10-27 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201027_0507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='apartment_numer',
            new_name='apartment_number',
        ),
    ]
