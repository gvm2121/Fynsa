# Generated by Django 2.2.5 on 2021-03-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFL', '0018_auto_20210222_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='lva_vector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('familia', models.TextField(blank=True, null=True)),
                ('nemo', models.TextField(blank=True, null=True)),
                ('tir_lva', models.DecimalField(decimal_places=2, max_digits=12)),
                ('tipo_instrumento', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duracion', models.DecimalField(decimal_places=2, max_digits=5)),
                ('riesgo', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
