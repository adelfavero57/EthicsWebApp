
from django.urls import path
from . import views

urlpatterns = [
    path('', views.managelistPage, name='managelist'),

]
