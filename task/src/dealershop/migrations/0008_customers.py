# Generated by Django 3.2.7 on 2021-09-17 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealershop', '0007_auto_20210917_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('SSN', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='SSN')),
                ('Name', models.CharField(blank=True, max_length=15)),
                ('phone', models.PositiveIntegerField(blank=True)),
            ],
        ),
    ]