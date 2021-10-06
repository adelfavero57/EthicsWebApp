from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.db.models.fields import IntegerField
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from accounts.models import CoverSheetQuestion
from accounts.models import CoverSheetAnswers
from accounts.models import Application
from .forms import CoverSheetForm
from django.http import HttpResponse


# Create your views here.



def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['researcher'])
def coversheetPage(request, newapplication_id):
    
    
    if request.method == 'POST':
        
        summary_text = request.POST['summary']
        # summary_text = coversheet_form.cleaned_data['summary']
        # csq_id_1001 = CoverSheetQuestion.objects.get(pk=1001)
        # Summary = CoverSheetAnswers.objects.create(text = summary_text, question_id = csq_id_1001, application_id = new_application, is_short_answer = True)

    
        # protocol_text = coversheet_form.cleaned_data['protocol']
        # csq_id_1002 = CoverSheetQuestion.objects.get(pk=1002)
        # Protocol = CoverSheetAnswers.objects.create(text = protocol_text, question_id = csq_id_1002, application_id = new_application, is_short_answer = True)
    

        # investigatorname_text = coversheet_form.cleaned_data['investigatorname']
        # csq_id_1003 = CoverSheetQuestion.objects.get(pk=1003)
        # Investigatorname = CoverSheetAnswers.objects.create(text = investigatorname_text, question_id = csq_id_1003, application_id = new_application, is_short_answer = True)
    

        # investigatorid_text = coversheet_form.cleaned_data['investigatorid']
        # csq_id_1004 = CoverSheetQuestion.objects.get(pk=1004)
        # Investigatorid = CoverSheetAnswers.objects.create(text = investigatorid_text, question_id = csq_id_1004, application_id = new_application, is_short_answer = True)
    

        # center_text = coversheet_form.cleaned_data['center']
        # csq_id_1005 = CoverSheetQuestion.objects.get(pk=1005)
        # Center = CoverSheetAnswers.objects.create(text = center_text, question_id = csq_id_1005, application_id = new_application, is_short_answer = True)
        

        # role_text = coversheet_form.cleaned_data['role']
        # csq_id_1006 = CoverSheetQuestion.objects.get(pk=1006)
        # Role = CoverSheetAnswers.objects.create(text = role_text, question_id = csq_id_1006, application_id = new_application, is_short_answer = False)
    

        # otherinternalinvestigators_text = coversheet_form.cleaned_data['otherinternalinvestigators']
        # csq_id_1007 = CoverSheetQuestion.objects.get(pk=1007)
        # Otherinternalinvestigators = CoverSheetAnswers.objects.create(text = otherinternalinvestigators_text, question_id = csq_id_1007, application_id = new_application, is_short_answer = False)
        

        # internalinvestigatorsnumber_text = coversheet_form.cleaned_data['internalinvestigatorsnumber']
        # csq_id_1008 = CoverSheetQuestion.objects.get(pk=1008)
        # Internalinvestigatorsnumber = CoverSheetAnswers.objects.create(text = internalinvestigatorsnumber_text, question_id = csq_id_1008, application_id = new_application, is_short_answer = False)
        

        # otherexternalinvestigators_text = coversheet_form.cleaned_data['otherexternalinvestigators']
        # csq_id_1009 = CoverSheetQuestion.objects.get(pk=1009)
        # Otherexternalinvestigators = CoverSheetAnswers.objects.create(text = otherexternalinvestigators_text, question_id = csq_id_1009, application_id = new_application, is_short_answer = False)
    

        # externalinvestigatorsnumber_text = coversheet_form.cleaned_data['externalinvestigatorsnumber']
        # csq_id_1010 = CoverSheetQuestion.objects.get(pk=1010)
        # Externalinvestigatorsnumber = CoverSheetAnswers.objects.create(text = externalinvestigatorsnumber_text, question_id = csq_id_1010, application_id = new_application, is_short_answer = False)
        

        # responsible_text = coversheet_form.cleaned_data['responsible']
        # csq_id_1011 = CoverSheetQuestion.objects.get(pk=1011)
        # Responsible = CoverSheetAnswers.objects.create(text = responsible_text, question_id = csq_id_1011, application_id = new_application, is_short_answer = True)
    

        # currentstate_text = coversheet_form.cleaned_data['currentstate']
        # csq_id_1012 = CoverSheetQuestion.objects.get(pk=1012)
        # Currentstate = CoverSheetAnswers.objects.create(text = currentstate_text, question_id = csq_id_1012, application_id = new_application, is_short_answer = True)
        

        # HRECname_text = coversheet_form.cleaned_data['HRECname']
        # csq_id_1013 = CoverSheetQuestion.objects.get(pk=1013)
        # hRECname = CoverSheetAnswers.objects.create(text = HRECname_text, question_id = csq_id_1013, application_id = new_application, is_short_answer = True)
        

        # action_text = coversheet_form.cleaned_data['action']
        # csq_id_1014 = CoverSheetQuestion.objects.get(pk=1014)
        # Action = CoverSheetAnswers.objects.create(text = action_text, question_id = csq_id_1014, application_id = new_application, is_short_answer = True)
        # #Action.save()

        # title_text = coversheet_form.cleaned_data['title']
        # csq_id_1015 = CoverSheetQuestion.objects.get(pk=1015)
        # Title = CoverSheetAnswers.objects.create(text = title_text, question_id = csq_id_1015, application_id = new_application, is_short_answer = True)
        #     #Title.save()

        # contractaction_text = coversheet_form.cleaned_data['contractaction']
        # csq_id_1016 = CoverSheetQuestion.objects.get(pk=1016)
        # Contractaction = CoverSheetAnswers.objects.create(text = contractaction_text, question_id = csq_id_1016, application_id = new_application, is_short_answer = True)
        

        # otherrelevantdetails_text = coversheet_form.cleaned_data['otherrelevantdetails']
        # csq_id_1017 = CoverSheetQuestion.objects.get(pk=1017)
        # Otherrelevantdetails = CoverSheetAnswers.objects.create(text = otherrelevantdetails_text, question_id = csq_id_1017, application_id = new_application, is_short_answer = True)
        
        return redirect('questionnaire', newapplication_id.pk)






    cover = CoverSheetQuestion.objects.all()
    context = {'cover': cover, 'application_id': newapplication_id}
    return render(request, 'coversheet.html', context)




    




