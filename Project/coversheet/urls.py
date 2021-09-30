from django.urls import path
from . import views
from accounts.views import editUserPage





urlpatterns = [
    path('', views.coversheetPage, name='coversheet'),
    path('logout/', views.logout_view, name='logout'),
<<<<<<< HEAD
    path('edit_profile/', editUserPage, name='editprofile'),
=======
    path('edit_profile/', editUserPage, name='editprofile')
>>>>>>> 3f455360ff42d02ad6c646f72bf96ab9cbba2756
]