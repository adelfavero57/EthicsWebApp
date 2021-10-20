from django.shortcuts import render
from accounts.models import Application
from django.views.generic import DetailView, UpdateView
#lock behind authentication barrier
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




