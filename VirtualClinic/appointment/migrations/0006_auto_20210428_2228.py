# Generated by Django 3.1.4 on 2021-04-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_doctor_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
