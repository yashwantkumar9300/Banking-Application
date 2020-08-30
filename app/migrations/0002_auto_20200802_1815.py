# Generated by Django 3.0.7 on 2020-08-02 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acno', models.IntegerField(default=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('reference', models.IntegerField(default=True)),
                ('particular', models.CharField(default=True, max_length=50)),
                ('credit', models.FloatField(default='')),
                ('debit', models.FloatField(default='')),
                ('balance', models.FloatField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='savingaccount',
            name='balance',
            field=models.FloatField(default='0.0'),
        ),
        migrations.AddField(
            model_name='savingaccount',
            name='password',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='savingaccount',
            name='status',
            field=models.CharField(default='Active', max_length=20),
        ),
        migrations.AlterField(
            model_name='admin',
            name='address',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='admin',
            name='contact',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='email',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='admin',
            name='name',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='admin',
            name='uname',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='adhar',
            field=models.IntegerField(default=True, unique=True),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='city',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='dist',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='dob',
            field=models.DateField(default=True),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='email',
            field=models.CharField(default=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='fname',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='ftname',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='gender',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='house',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='lname',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='mname',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='mobile',
            field=models.IntegerField(default=True, unique=True),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='national',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='photo',
            field=models.ImageField(default=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='pin',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='post',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='sign',
            field=models.ImageField(default=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='state',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='street',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='savingaccount',
            name='village',
            field=models.CharField(default=True, max_length=50),
        ),
    ]
