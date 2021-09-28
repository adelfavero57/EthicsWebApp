from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from accounts.decorators import allowed_users
from django.shortcuts import render, redirect
from accounts.models import Question
# Create your views here.


def welcome(request):
    # Will have to add login required and researcher role later
    if request.method == 'POST':
        return redirect('quiz')
    return render(request, 'welcome.html')


def quiz(request):
    questions = Question.objects.all().filter(section_name="B")
    if request.method == 'POST':
        # if one answer is yes, return fail otherwise redirect to ethics welcome.
        for i in range(201, len(questions)+201):
            selection = request.POST.get('selection{}'.format(i))
            if selection == 'Yes':
                return HttpResponse('Failure')
        return HttpResponse('Success')

    context = {'questions': questions}
    return render(request, 'quiz.html', context)
