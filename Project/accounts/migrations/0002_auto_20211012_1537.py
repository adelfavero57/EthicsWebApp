# Generated by Django 3.2.7 on 2021-10-12 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='PCF',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='application',
            name='PIS',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]