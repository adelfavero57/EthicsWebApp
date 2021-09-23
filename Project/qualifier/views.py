from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.shortcuts import render, redirect
# Create your views here.


def welcome(request):
    # Will have to add login required and researcher role later
    if request.method == 'POST':
        return redirect('quiz')
    return render(request, 'welcome.html')


def quiz(request):
    context = {}
    return render(request, 'quiz.html', context)
