# Generated by Django 2.2.5 on 2021-06-03 12:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFI', '0007_rfi_bonos'),
    ]

    operations = [
        migrations.CreateModel(
            name='PruebaArrayModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riesgo', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None)),
            ],
        ),
    ]
