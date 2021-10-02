from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.decorators import allowed_users
from accounts.models import Application
# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def approve(request, item_id):

    item = Application.objects.get(pk=item_id)
    item.status = 'approved'
    item.save()

    return redirect('approvelist')


@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def disapprove(request, item_id):

    item = Application.objects.get(pk=item_id)
    item.status = 'disapproved'
    item.save()

    return redirect('approvelist')


@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def approvelistPage(request):

    applications = Application.objects.all()

    context = {'applications': applications}
    return render(request, 'approvelist.html', context)
