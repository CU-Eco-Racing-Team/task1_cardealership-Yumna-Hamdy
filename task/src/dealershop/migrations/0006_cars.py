# Generated by Django 3.2.7 on 2021-09-16 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealershop', '0005_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model', models.CharField(blank=True, max_length=15)),
                ('Price', models.PositiveIntegerField(blank=True)),
                ('Plate_No', models.CharField(blank=True, max_length=15)),
                ('Contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dealershop.contract')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cars', to='dealershop.customers')),
                ('Industries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cars', to='dealershop.industries')),
            ],
        ),
    ]