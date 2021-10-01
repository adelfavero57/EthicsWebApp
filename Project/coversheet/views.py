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

        Application.objects.create(user = request.user, title = 'fix the of twice application', supervisor = 'shuai', status = 'in progress')
        a_id = Application.objects.latest('id')
        
        summary_text = request.POST['summary']
        csq_id_1001 = CoverSheetQuestion.objects.get(pk=1001)
        Summary = CoverSheetAnswers.objects.create(text = summary_text, question_id = csq_id_1001, application_id = a_id, is_short_answer = True)
        #Summary.save()

      
        protocol_text = request.POST['protocol']
        csq_id_1002 = CoverSheetQuestion.objects.get(pk=1002)
        Protocol = CoverSheetAnswers.objects.create(text = protocol_text, question_id = csq_id_1002, application_id = a_id, is_short_answer = True)
        #Protocol.save()

        investigatorname_text = request.POST['investigatorname']
        csq_id_1003 = CoverSheetQuestion.objects.get(pk=1003)
        Investigatorname = CoverSheetAnswers.objects.create(text = investigatorname_text, question_id = csq_id_1003, application_id = a_id, is_short_answer = True)
        #Investigatorname.save()

        investigatorid_text = request.POST['investigatorid']
        csq_id_1004 = CoverSheetQuestion.objects.get(pk=1004)
        Investigatorid = CoverSheetAnswers.objects.create(text = investigatorid_text, question_id = csq_id_1004, application_id = a_id, is_short_answer = True)
        #Investigatorid.save()

        center_text = request.POST['center']
        csq_id_1005 = CoverSheetQuestion.objects.get(pk=1005)
        Center = CoverSheetAnswers.objects.create(text = center_text, question_id = csq_id_1005, application_id = a_id, is_short_answer = True)
        #Center.save()

        role_text = request.POST['role']
        csq_id_1006 = CoverSheetQuestion.objects.get(pk=1006)
        Role = CoverSheetAnswers.objects.create(text = role_text, question_id = csq_id_1006, application_id = a_id, is_short_answer = False)
        #Role.save()

        otherinternalinvestigators_text = request.POST['otherinternalinvestigators']
        csq_id_1007 = CoverSheetQuestion.objects.get(pk=1007)
        Otherinternalinvestigators = CoverSheetAnswers.objects.create(text = otherinternalinvestigators_text, question_id = csq_id_1007, application_id = a_id, is_short_answer = False)
        #Otherinternalinvestigators.save()

        internalinvestigatorsnumber_text = request.POST['internalinvestigatorsnumber']
        csq_id_1008 = CoverSheetQuestion.objects.get(pk=1008)
        Internalinvestigatorsnumber = CoverSheetAnswers.objects.create(text = internalinvestigatorsnumber_text, question_id = csq_id_1008, application_id = a_id, is_short_answer = False)
        #Internalinvestigatorsnumber.save()

        otherexternalinvestigators_text = request.POST['otherexternalinvestigators']
        csq_id_1009 = CoverSheetQuestion.objects.get(pk=1009)
        Otherexternalinvestigators = CoverSheetAnswers.objects.create(text = otherexternalinvestigators_text, question_id = csq_id_1009, application_id = a_id, is_short_answer = False)
        #Otherexternalinvestigators.save()

        externalinvestigatorsnumber_text = request.POST['externalinvestigatorsnumber']
        csq_id_1010 = CoverSheetQuestion.objects.get(pk=1010)
        Externalinvestigatorsnumber = CoverSheetAnswers.objects.create(text = externalinvestigatorsnumber_text, question_id = csq_id_1010, application_id = a_id, is_short_answer = False)
        #Externalinvestigatorsnumber.save()

        responsible_text = request.POST['responsible']
        csq_id_1011 = CoverSheetQuestion.objects.get(pk=1011)
        Responsible = CoverSheetAnswers.objects.create(text = responsible_text, question_id = csq_id_1011, application_id = a_id, is_short_answer = True)
        #Responsible.save()

        currentstate_text = request.POST['currentstate']
        csq_id_1012 = CoverSheetQuestion.objects.get(pk=1012)
        Currentstate = CoverSheetAnswers.objects.create(text = currentstate_text, question_id = csq_id_1012, application_id = a_id, is_short_answer = True)
        #Currentstate.save()

        HRECname_text = request.POST['HRECname']
        csq_id_1013 = CoverSheetQuestion.objects.get(pk=1013)
        hRECname = CoverSheetAnswers.objects.create(text = HRECname_text, question_id = csq_id_1013, application_id = a_id, is_short_answer = True)
        #hRECname.save()

        action_text = request.POST['action']
        csq_id_1014 = CoverSheetQuestion.objects.get(pk=1014)
        Action = CoverSheetAnswers.objects.create(text = action_text, question_id = csq_id_1014, application_id = a_id, is_short_answer = True)
        #Action.save()

        title_text = request.POST['title']
        csq_id_1015 = CoverSheetQuestion.objects.get(pk=1015)
        Title = CoverSheetAnswers.objects.create(text = title_text, question_id = csq_id_1015, application_id = a_id, is_short_answer = True)
        #Title.save()

        contractaction_text = request.POST['contractaction']
        csq_id_1016 = CoverSheetQuestion.objects.get(pk=1016)
        Contractaction = CoverSheetAnswers.objects.create(text = contractaction_text, question_id = csq_id_1016, application_id = a_id, is_short_answer = True)
        #Contractaction.save()

        otherrelevantdetails_text = request.POST['otherrelevantdetails']
        csq_id_1017 = CoverSheetQuestion.objects.get(pk=1017)
        Otherrelevantdetails = CoverSheetAnswers.objects.create(text = otherrelevantdetails_text, question_id = csq_id_1017, application_id = a_id, is_short_answer = True)
        #Otherrelevantdetails.save()

        return redirect('questionnaire', application_id = a_id)

    cover = CoverSheetQuestion.objects.all()
    context = {'cover': cover}
    return render(request, 'coversheet.html', context)




    




