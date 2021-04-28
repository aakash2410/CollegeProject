# Generated by Django 3.1.4 on 2021-04-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20210428_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='doctor',
            name='fees',
            field=models.FloatField(default=1000.0),
        ),
    ]
