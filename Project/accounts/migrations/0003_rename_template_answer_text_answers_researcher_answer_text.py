# Generated by Django 3.2.7 on 2021-11-01 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211031_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='template_answer_text',
            new_name='researcher_answer_text',
        ),
    ]
