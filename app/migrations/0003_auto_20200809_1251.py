# Generated by Django 3.0.7 on 2020-08-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200802_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='credit',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='statement',
            name='debit',
            field=models.FloatField(default=0.0),
        ),
    ]
