from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminlistPage, name='adminlist'),
    path('logout/', views.logout_view, name='logout')
]
