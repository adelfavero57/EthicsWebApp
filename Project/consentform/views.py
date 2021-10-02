from accounts.models import CoverSheetAnswers
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from accounts.models import CoverSheetQuestion
from accounts.models import Answers
from accounts.models import Application
# Create your views here.
from .utils import render_to_pdf



def logout_view(request):
    logout(request)
    return redirect('login')




@login_required(login_url='login')
def Consentform(request):
    consent = CoverSheetAnswers.objects.all()
    context = {'consent': consent}
    pdf = render_to_pdf('form.html', context)
    return pdf
    #return render(request, 'form.html', context)



