# Generated by Django 2.0.5 on 2018-06-06 16:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180604_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
