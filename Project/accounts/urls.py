from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# URLconf
urlpatterns = [
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('home/', views.homePage),
    path('edit_profile/', views.editUserPage),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
