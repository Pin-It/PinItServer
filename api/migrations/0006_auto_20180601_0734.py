# Generated by Django 2.0.5 on 2018-06-01 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180601_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=18),
        ),
        migrations.AlterField(
            model_name='pin',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=18),
        ),
    ]
