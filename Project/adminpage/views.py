from django.http import request
from django.shortcuts import render, redirect
from accounts.decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def adminPage(request):
    return render(request, 'adminpage.html')
