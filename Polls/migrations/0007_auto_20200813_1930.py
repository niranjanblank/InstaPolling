# Generated by Django 3.0.7 on 2020-08-13 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0006_auto_20200808_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
    ]