# Generated by Django 4.0.5 on 2023-07-16 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='gender',
        ),
    ]
