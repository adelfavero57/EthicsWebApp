from django.urls import path
from .views import PISform2, PCFform2, createPIS, createPCF

urlpatterns = [
    path('PIS/<int:pk>', PISform2.as_view(), name='information_sheet'),
    path('PCF/<int:pk>', PCFform2.as_view(), name='consent_form'),
    path('new_PIS/<int:pk>', createPIS.as_view(), name='new_PIS'),
    path('new_PCF/<int:pk>', createPCF.as_view(), name='new_PCF'),
]