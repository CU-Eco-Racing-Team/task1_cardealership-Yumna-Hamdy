# Generated by Django 3.2.7 on 2021-09-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealershop', '0019_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('Name', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Name')),
                ('phone', models.PositiveIntegerField(blank=True)),
            ],
        ),
    ]
