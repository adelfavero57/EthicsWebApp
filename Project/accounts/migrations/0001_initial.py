from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverSheetAnswers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CoverSheetQuestion',
            fields=[
                ('coversheetquestion_num', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('is_short_answer', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(

            name='Question',
            fields=[
                ('question_num', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('text', models.TextField()),
                ('is_short_answer', models.BinaryField()),
                ('section_name', models.CharField(max_length=1)),

                ('tips', models.TextField(default='', max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('title', models.TextField(max_length=200)),
                ('supervisor', models.TextField(max_length=150)),
                ('is_complete', models.BinaryField()),
                ('is_approved', models.BinaryField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('is_short_answer', models.BinaryField()),
                ('section_name', models.CharField(max_length=1)),
                ('is_referenced', models.BinaryField()),
                ('is_exemplar', models.BinaryField()),
                ('application_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.application')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.question')),
            ],
        ),
    ]
