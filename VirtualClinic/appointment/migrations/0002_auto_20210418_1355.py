# Generated by Django 3.1.4 on 2021-04-18 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='mobile_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='mobile_number',
            field=models.IntegerField(default=0),
        ),
    ]
