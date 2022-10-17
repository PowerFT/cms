# Generated by Django 4.1.1 on 2022-09-19 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('mainid', models.AutoField(primary_key=True, serialize=False)),
                ('companyname', models.CharField(max_length=30)),
                ('projectname', models.CharField(max_length=20)),
                ('contactperson', models.CharField(max_length=25)),
                ('phonenumber', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('countryname', models.CharField(max_length=20)),
                ('cityname', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('dateandtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('mainid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('amount', models.FloatField()),
                ('startdate', models.DateField()),
                ('duedate', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('clientname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.client')),
            ],
        ),
    ]