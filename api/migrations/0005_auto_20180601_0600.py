# Generated by Django 2.0.5 on 2018-06-01 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='by_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pin',
            name='by_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.UserProfile'),
            preserve_default=False,
        ),
    ]
