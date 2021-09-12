from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.

from .models import Application


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def managelistPage(request):

    applications = Application.objects.filter(user=request.user)
    context = {'applications': applications}
    
    return render(request, 'managelist.html', context)


@login_required(login_url='login')

def createPage(request):


    return render(request, 'newpag')
