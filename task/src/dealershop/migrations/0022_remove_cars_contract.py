# Generated by Django 3.2.7 on 2021-09-17 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dealershop', '0021_cars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='Contract',
        ),
    ]