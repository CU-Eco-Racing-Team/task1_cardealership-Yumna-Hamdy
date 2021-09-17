# Generated by Django 3.2.7 on 2021-09-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealershop', '0027_auto_20210917_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealers',
            fields=[
                ('Name', models.CharField(blank=True, max_length=15)),
                ('SSN', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='SSN')),
                ('phone', models.PositiveIntegerField(blank=True)),
                ('Is_owner', models.BooleanField(blank=True, default=False)),
                ('Can_buy_car', models.BooleanField(default=False)),
                ('Can_sign_contract', models.BooleanField(default=False)),
                ('Can_sell_car', models.BooleanField(default=False)),
                ('Can_change_price', models.BooleanField(default=False)),
                ('Contract', models.ManyToManyField(blank=True, related_name='Dealers', to='dealershop.Contract')),
            ],
        ),
    ]
