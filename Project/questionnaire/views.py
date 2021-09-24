from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.shortcuts import get_object_or_404, render, redirect
from accounts.models import Application, Question, Answers
from django.http import HttpResponse
# Create your views here.


def questionnaire(request):
    # Will have to add login required and researcher role later
    #que = Question.objects.get(question_num=2)
    que = Question
    context = {'que':que}
    return render(request, 'questionnaire.html', context)