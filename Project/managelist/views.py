from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.shortcuts import render, redirect
from accounts.models import Application
# Create your views here.





def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def managelistPage(request):
    applications = []

    if request.method == "POST":

        search_text = request.POST["search_text"]

        if search_text is not None:

            print(search_text)

            applications = Application.objects.filter(user=request.user, title=search_text)
        
        else:

            applications = Application.objects.filter(user=request.user)
    
    else:

        applications = Application.objects.filter(user=request.user)
    
    
    context = {'applications': applications}

    return render(request, 'managelist.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])

def deleteRow(request, item_id):

    item = Application.objects.get(id=item_id)

    item.delete()

    return redirect('managelist')







