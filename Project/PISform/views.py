from accounts.models import CoverSheetAnswers
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from accounts.models import CoverSheetQuestion
from accounts.models import Answers
from accounts.models import Application
# Create your views here.


class Application:
    def __init__(self, name, process, status):

        self.name = name
        self.process = process
        self.status = status



def logout_view(request):
    logout(request)
    return redirect('login')




@login_required(login_url='login')
def PISform(request):
    pis1 = CoverSheetAnswers.objects.all()
    pis2 = Answers.objects.all()
    context = {'pis': pis1}
    return render(request, 'PISform.html', context)
    #return render(request, 'PISform.html')


