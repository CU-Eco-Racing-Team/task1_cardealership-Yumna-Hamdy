# Generated by Django 3.2.7 on 2021-09-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealershop', '0028_dealers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('Name', models.CharField(blank=True, max_length=15)),
                ('SSN', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='SSN')),
                ('phone', models.PositiveIntegerField(blank=True)),
            ],
        ),
    ]