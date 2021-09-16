from django.contrib.auth import logout
import accounts.views as accounts
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def approvelistPage(request):

    context = {}
    return render(request, 'approvelist.html', context)
