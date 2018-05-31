# Generated by Django 2.0.5 on 2018-05-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_type', models.CharField(choices=[('PICKPOCKET', 'Pickpocket'), ('DRUNK', 'Drunk'), ('ROBBERY', 'Robbery'), ('SCAM', 'Scam'), ('HARASSMENT', 'Harassment'), ('OTHERS', 'Others')], max_length=10)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]