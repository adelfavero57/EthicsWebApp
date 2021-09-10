from django.urls import path
from . import views

# URLconf
urlpatterns = [
    path('', views.redirect_view),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('home/', views.homePage, name='home'),
]
