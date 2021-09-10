from django.urls import path
from . import views
from .views import UserEditView

# URLconf
urlpatterns = [
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('home/', views.homePage),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
