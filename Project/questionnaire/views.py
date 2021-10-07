from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.shortcuts import get_object_or_404, render, redirect
from accounts.models import Application, Question, Answers
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def questionnaire(request, application_id):
    
    a_id = Application.objects.get(pk=application_id)
    questions = Question.objects.all()
    #print(request.method)
    if request.method == 'POST':

        
        for i in questions:
            if i.question_num == 905:
                break

        a_id.status = "COMPLETE"

        a_id.save()
        
        return redirect('managelist')

    
            
    #que = Question.objects.get(question_num=2)
    que = Question.objects.all()
    answers = Answers.objects.all()
    context = {'que':que, 'answers': answers}
    return render(request, 'questionnaire.html', context)