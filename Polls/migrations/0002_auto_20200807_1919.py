# Generated by Django 3.0.7 on 2020-08-07 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Options',
            new_name='Option',
        ),
    ]
