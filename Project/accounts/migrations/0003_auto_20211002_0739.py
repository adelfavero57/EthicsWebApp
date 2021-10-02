# Generated by Django 3.2.6 on 2021-10-02 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_application_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='text',
        ),
        migrations.AddField(
            model_name='answers',
            name='multiple_choice_answer',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='answers',
            name='short_answer_text',
            field=models.TextField(null=True),
        ),
    ]
