# Generated by Django 3.2.7 on 2021-09-16 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealershop', '0003_contract'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('Name', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Name')),
                ('phone', models.PositiveIntegerField(blank=True)),
            ],
        ),
    ]
