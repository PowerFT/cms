# Generated by Django 4.1.1 on 2022-09-20 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='projectname',
        ),
    ]
