from django.urls import path
from . import views
from accounts.views import editUserPage

urlpatterns = [
    path('', views.managelistPage, name='managelist'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', editUserPage, name='editprofile'),
    path('<item_id>/', views.deleteRow, name='delete')
    #path('search/', views.search, name='search')
]
