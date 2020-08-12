# Generated by Django 3.0.7 on 2020-08-08 10:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0004_option_votes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-date_published']},
        ),
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]