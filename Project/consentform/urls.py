from django.urls import path
from . import views
from accounts.views import editUserPage


urlpatterns = [
    path('', views.Consentform, name='consentform'),
    path('logout/', views.logout_view, name='logout'),
]
