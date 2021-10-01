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
    print(application_id)
    a_id = Application.objects.get(pk=application_id)
    questions = Question.objects.all()
    #print(request.method)
    if request.method == 'POST':
        for i in questions:
            print(i.question_num)
            if i.question_num == 905:
                return redirect('managelist')
            temp2 = str(i.question_num)
            temp = request.POST[temp2]
            
            temp_obj = Question.objects.get(pk = i.question_num)
            new_answer_obj = Answers.objects.create(text = temp, question_id = i, 
            application_id = a_id, is_short_answer = 0, section_name = i.section_name)
        
        return redirect('managelist')
            
    #que = Question.objects.get(question_num=2)
    que = Question.objects.all()
    context = {'que':que}
    return render(request, 'questionnaire.html', context)