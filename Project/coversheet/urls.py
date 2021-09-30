from django.urls import path
from . import views
from accounts.views import editUserPage





urlpatterns = [
    path('', views.coversheetPage, name='coversheet'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', editUserPage, name='editprofile'),
]