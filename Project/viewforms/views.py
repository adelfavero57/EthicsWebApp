from django.shortcuts import render
from accounts.models import Application
from django.views.generic import DetailView, UpdateView
from .utils import render_to_pdf
#lock behind authentication barrier


#@login_required(login_url='login')
#def PISform2(request, application_id):
 #   pis1 = Application.PIS_rt
  #  context = {'pis': pis1}
   # pdf = render_to_pdf('information_sheet.html', context, application_id)
    #return render(request, 'PISform.html', context)
    #return render(request, 'PISform.html')
    #return pdf

class PISform2(DetailView):
    model = Application
    template_name = 'information_sheet.html'

class PCFform2(DetailView):
    model = Application
    template_name = 'consent_form.html'

class createPIS(UpdateView):
    model = Application
    fields = ['PIS_rt']
    template_name = 'new_PIS.html'

class createPCF(UpdateView):
    model = Application
    fields = ['PCF_rt']
    template_name = 'new_PCF.html'




