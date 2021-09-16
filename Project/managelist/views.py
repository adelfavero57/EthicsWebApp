from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.shortcuts import render, redirect
# Create your views here.
from .models import Application






def logout_view(request):
    logout(request)
    return redirect('login')

    return render(request, 'managelist.html', context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=[])
def managelistPage(request):

    
    applications = Application.objects.filter(user=request.user)
    context = {'applications': applications}

    return render(request, 'managelist.html', context)


@login_required(login_url='login')
def managelistPage(request):
    
    applications = Application.objects.filter(user=request.user)
    context = {'applications': applications}

    return render(request, 'managelist.html', context)