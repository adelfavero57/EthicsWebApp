from django.urls import path
from . import views

urlpatterns = [
    path('', views.approvelistPage, name='approvelist'),
    path('logout/', views.logout_view, name='logout')
]
