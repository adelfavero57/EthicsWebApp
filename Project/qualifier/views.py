from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.shortcuts import render, redirect
# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')
