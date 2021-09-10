from django.urls import path
from . import views

# URLconf
urlpatterns = [
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('home/', views.homePage),
    path('edit_profile/', views.editUserPage),
]
