# Generated by Django 3.2.5 on 2022-03-12 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_vaccinestock'),
        ('vaccine', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vaccines',
            new_name='Vaccine',
        ),
    ]
