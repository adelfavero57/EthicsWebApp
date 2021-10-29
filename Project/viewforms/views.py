from django.shortcuts import render
from accounts.models import Application
from django.views.generic import DetailView, UpdateView
from .utils import render_to_pdf
from django.shortcuts import render, redirect
from .forms import PISform, PCFform
#lock behind authentication barrier


#@login_required(login_url='login')
#def PISform2(request, application_id):
 #   pis1 = Application.PIS_rt
  #  context = {'pis': pis1}
   # pdf = render_to_pdf('information_sheet.html', context, application_id)
    #return render(request, 'PISform.html', context)
    #return render(request, 'PISform.html')
    #return pdf

#class PISform2(DetailView):
    #model = Application
    #template_name = 'information_sheet.html'
 
# pass id attribute from urls
def PISform2(request, application_id):
    # dictionary for initial data with
    # field names as keys
    context ={
        'data': Application.objects.get(pk=application_id),
        'application_id': application_id
    }
 
    return render(request, "information_sheet.html", context)

class PCFform2(DetailView):
    model = Application
    template_name = 'consent_form.html'

#class createPIS(UpdateView):
    #model = Application
    #fields = ['PIS_rt']
    #readonly_fields = ['id']
    #template_name = 'new_PIS.html'

def createPIS(request, application_id):
    application = Application.objects.get(pk=application_id)
    form = PISform(instance=Application.objects.get(pk=application_id))
    if request.method == 'POST':
        form = PISform(request.POST, instance=Application.objects.get(pk=application_id))
        if form.is_valid():
            form.save(commit=True)
        #pis_text = request.POST['pis']
        #application.pis_rt = pis_text
        #application.pis_rt.save()
        #return redirect('questionnaire', application_id)
    context = {
        'form':form,
        'application_id': application_id
    }
    return render(request, 'new_PIS.html', context)


def createPCF(request, application_id):
    form = PCFform(instance=Application.objects.get(pk=application_id))
    if request.method == 'POST':
        form = PCFform(request.POST, instance=Application.objects.get(pk=application_id))
        if form.is_valid():
            form.save(commit=True)
        #pis_text = request.POST['pis']
        #application.pis_rt = pis_text
        #application.pis_rt.save()
        #return redirect('questionnaire', application_id)
    context = {
        'form':form,
        'application_id': application_id
    }
    return render(request, 'new_PCF.html', context)


#class createPCF(UpdateView):
 #   model = Application
  #  fields = ['PCF_rt']
   # readonly_fields = ['id']
    #template_name = 'new_PCF.html'




