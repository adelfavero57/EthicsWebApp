from django.urls import path
from . import views
from accounts.views import editUserPage
from questionnaire.views import questionnaire


urlpatterns = [
    path('<newapplication_id>', views.coversheetPage, name='coversheet'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', editUserPage, name='editprofile'),
    path('<newapplication_id>', questionnaire, name="questionnaire")

]
