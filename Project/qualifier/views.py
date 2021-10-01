
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.shortcuts import render, redirect
from accounts.models import Question
# Create your views here.


@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def welcome(request):
    # Will have to add login required and researcher role later
    if request.method == 'POST':
        return redirect('quiz')
    return render(request, 'welcome.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def failure(request):
    if request.method == 'POST':
        return redirect('managelist')
    return render(request, 'failure.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def success(request):
    if request.method == 'POST':
        return redirect('coversheet')
    return render(request, 'success.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def quiz(request):
    questions = Question.objects.all().filter(section_name="B")
    if request.method == 'POST':
        # if one answer is yes, return fail otherwise redirect to ethics welcome.
        for i in range(201, len(questions)+201):
            selection = request.POST.get('selection{}'.format(i))
            if selection == 'Yes':
                return redirect('failure')
        return redirect('success')

    context = {'questions': questions}
    return render(request, 'quiz.html', context)
