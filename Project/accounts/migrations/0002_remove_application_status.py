# Generated by Django 3.2.7 on 2021-10-01 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='status',
        ),
    ]
