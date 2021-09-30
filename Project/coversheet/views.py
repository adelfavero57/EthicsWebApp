from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from accounts.models import CoverSheetQuestion
from accounts.models import CoverSheetAnswers
from accounts.models import Application
# Create your views here.



def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def coversheetPage(request):
    # if request.method == "POST":

    #     protocol = request.POST['protocol']

    

    #         a = CoverSheetQuestion.objects.get(pk=1002)
    #         b = Application.objects.get(pk=1)

    #         protocol = CoverSheetAnswers.objects.create(text=protocol, question_id=a, application_id=b)

    #         protocol.save()


    cover = CoverSheetQuestion.objects.all()
    context = {'cover': cover}
    return render(request, 'coversheet.html', context)




    




