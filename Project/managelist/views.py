from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.

from .models import Application


class Application:
    def __init__(self, name, process, status):

        self.name = name
        self.process = process
        self.status = status


test1 = Application("form1", "20%", "IN PROCESS")
test2 = Application("form2", "20%", "IN PROCESS")
test3 = Application("form3", "20%", "IN PROCESS")
test4 = Application("form4", "20%", "IN PROCESS")
test5 = Application("form5", "20%", "IN PROCESS")



def managelistPage(request):

    
    
    username = request.user.name
    
    applications = Applications.objects.filter(username=username)

    #get data


def logout_view(request):
    logout(request)
    return redirect('login')

    return render(request, 'managelist.html', context)


@login_required(login_url='login')
def managelistPage(request):


    context = {'applications': Applications}
    return render(request, 'managelist.html', context)

