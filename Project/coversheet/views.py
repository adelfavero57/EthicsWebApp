from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from accounts.models import CoverSheetQuestion
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
def coversheetPage(request):
    cover = CoverSheetQuestion.objects.all()
    context = {'cover': cover}
    return render(request, 'coversheet.html', context)

