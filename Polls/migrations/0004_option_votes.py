# Generated by Django 3.0.7 on 2020-08-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0003_auto_20200807_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
