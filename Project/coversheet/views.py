from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models.fields import IntegerField
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
    if request.method == 'POST':
        summary_text = request.POST['summary']
        csq_id = CoverSheetQuestion.objects.get(pk=1001)
        a_id = Application.objects.get(pk=5)
        Summary = CoverSheetAnswers.objects.create(text = summary_text, question_id = csq_id, application_id = a_id, is_short_answer = True)
        Summary.save()

      
        Protocol_Title_text = request.POST['protocol']
        csq_id = CoverSheetQuestion.objects.get(pk=1002)
        a_id = Application.objects.get(pk=5)
        Protocol_Title = CoverSheetAnswers.objects.create(text = Protocol_Title_text, question_id = csq_id, application_id = a_id, is_short_answer = True)
        Protocol_Title.save()
    

    cover = CoverSheetQuestion.objects.all()
    context = {'cover': cover}
    return render(request, 'coversheet.html', context)

