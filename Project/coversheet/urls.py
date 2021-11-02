from django.urls import path
from . import views
from accounts.views import editUserPage
from questionnaire.views import questionnaire
from viewforms.views import PISform2, PCFform2, createPIS, createPCF

urlpatterns = [
    path('<newapplication_id>', views.coversheetPage, name='coversheet'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', editUserPage, name='editprofile'),
    path('<application_id>', questionnaire, name="questionnaire"),
    
    path('PIS/<int:pk>', PISform2.as_view(), name='information_sheet'),
    path('PCF/<int:pk>', PCFform2.as_view(), name='consent_form'),
    path('new_PIS/<int:pk>', createPIS.as_view(), name='new_PIS'),
    path('new_PCF/<int:pk>', createPCF.as_view(), name='new_PCF'),
]
