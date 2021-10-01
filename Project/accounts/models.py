from typing import cast
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import UUIDField
import uuid
from django.db.models.fields.related import ForeignKey
# Create your models here.

class Application(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, editable=False, null=False)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=200, null=False)
    supervisor = models.TextField(max_length=150, null=False)
    status = models.TextField(max_length=10)
    

class Question(models.Model):
    question_num = models.IntegerField(primary_key=True, unique=True, null=False)
    text = models.TextField(null=False)
    is_short_answer = models.IntegerField(null=False)
    section_name = models.CharField(max_length=1, null=False)
    tips = models.TextField(max_length=150, null=True, default='')

class Answers(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    text = models.TextField()
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    application_id = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True)
    is_short_answer = models.IntegerField(null=False)
    section_name = models.CharField(max_length=1, null=False)
    is_referenced = models.BinaryField(null=False)
    is_exemplar = models.BinaryField(null=False)
    #answer_type = models.TextField(null = True)

class CoverSheetQuestion(models.Model):
    question_num = models.IntegerField(primary_key=True, unique=True, null=False)
    text = models.TextField(null=False)
    is_short_answer = models.IntegerField(null=False)


class CoverSheetAnswers(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    question_id = models.ForeignKey(CoverSheetQuestion, on_delete=models.CASCADE)
    application_id = models.ForeignKey(Application, on_delete=models.CASCADE, null=True)
    is_short_answer = models.IntegerField(null=False)

