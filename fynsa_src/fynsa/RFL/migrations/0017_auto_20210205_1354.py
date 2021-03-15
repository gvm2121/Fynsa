# Generated by Django 2.2.5 on 2021-02-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFL', '0016_auto_20210205_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posiciones',
            name='dur_rskam',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='posiciones',
            name='marca',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True),
        ),
    ]