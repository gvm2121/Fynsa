# Generated by Django 2.2.5 on 2021-03-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFL', '0021_auto_20210305_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='supercintas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nemo', models.TextField(blank=True, null=True)),
                ('tasa_lva', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('tasa_rsk', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('tasa_lva_rsk_media', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('duracion', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('riesgo', models.TextField(blank=True, null=True)),
                ('descalce', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('familia', models.TextField(blank=True, null=True)),
                ('anotacion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
