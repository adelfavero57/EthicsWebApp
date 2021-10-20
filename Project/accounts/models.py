from typing import cast
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import UUIDField
import uuid
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

default_PCF_data = """<p>Project Name:</p>

<p>In giving my consent I acknowledge that:</p>

<p>1. The procedures required for the project and the time involved have been explained to me, and any questions I have about the project have been answered to my satisfaction.</p>

<p>2. I have read the Participant Information Statement and have been given the opportunity to discuss the information and my involvement in the project with the researcher/s.</p>

<p>3. I understand that being in this study is completely voluntary - I am not under any obligation to consent.</p>

<p>4. I understand that my involvement is strictly confidential. I understand that any research data gathered from the results of the study may be published however no information about me will be used in any way that is identifiable</p>

<p>5. I understand that I can withdraw from the study at any time, without affecting my relationship with the researcher(s) or the University of Sydney now or in the future.</p>

<p>6. I understand that I will be video and audio recorded as well as my screen interaction.</p>

<p>7. I understand that this is the first time participating in this study.</p>

<p>8. I agree that my rtecord of all clicks in my interaction on this interface will be shared on the Open Science Framework (OSF) platform so that other researchers can analyse them. This data will be de-identified so that it cannot be linked to me.</p>

<p>9. I understand that my video and audio recordings will only be used for analysis and will not be released.</p>
""" #Need to format this such that the spaces carry through to rtf

class Application(models.Model):

    id = models.IntegerField(
    primary_key=True, unique=True, editable=False, null=False)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=200, null=True)
    supervisor = models.TextField(max_length=150, null=True)
    status = models.TextField(max_length=20, null=True, default = "IN PROGRESS")
    PIS_rt = RichTextField(blank=True, null=True)
    PCF_rt = RichTextField(blank=True, null=True, default=default_PCF_data)



    def get_absolute_url(self):
        return reverse('questionnaire', args=(str(self.id)))


class Question(models.Model):
    question_num = models.IntegerField(
    primary_key=True, unique=True, null=False)
    text = models.TextField(null=False)
    is_short_answer = models.IntegerField(null=False)
    section_name = models.CharField(max_length=1, null=False)
    tips = models.TextField(max_length=150, null=True, default='')


class Answers(models.Model):
    id = models.IntegerField(primary_key=True)
    short_answer_text = models.TextField(null=True)
    multiple_choice_answer = models.BooleanField(null=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    application_id = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True)
    is_short_answer = models.IntegerField(null=False)
    section_name = models.CharField(max_length=1, null=False)
    is_referenced = models.IntegerField(null=False)
    is_exemplar = models.IntegerField(null=False)
    answer_type = models.TextField(null = True)


class CoverSheetQuestion(models.Model):
    question_num = models.IntegerField(
        primary_key=True, unique=True, null=False)
    text = models.TextField(null=False)
    is_short_answer = models.IntegerField(null=False)


class CoverSheetAnswers(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    question_id = models.ForeignKey(
        CoverSheetQuestion, on_delete=models.CASCADE)
    application_id = models.ForeignKey(
        Application, on_delete=models.CASCADE, null=True)
    is_short_answer = models.IntegerField(null=False)
