# Generated by Django 2.2.5 on 2021-01-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFL', '0007_archivos_cintas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivos_cintas',
            name='rsk',
            field=models.FileField(upload_to='cintas/'),
        ),
        migrations.AlterField(
            model_name='archivos_cintas',
            name='tr',
            field=models.FileField(upload_to='cintas/'),
        ),
        migrations.AlterField(
            model_name='tr',
            name='cantidad',
            field=models.BigIntegerField(),
        ),
    ]