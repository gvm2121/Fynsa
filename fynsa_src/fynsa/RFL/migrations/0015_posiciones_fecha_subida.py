# Generated by Django 2.2.5 on 2021-02-04 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFL', '0014_remove_posiciones_fecha_subida'),
    ]

    operations = [
        migrations.AddField(
            model_name='posiciones',
            name='fecha_subida',
            field=models.DateField(auto_now=True),
        ),
    ]
