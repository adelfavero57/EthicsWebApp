from django.contrib import admin
from accounts.models import Application, Question, Answers, CoverSheetAnswers, CoverSheetQuestion
from django.contrib.auth.models import User, Group

class MyAdminSite(admin.AdminSite):

    site_header = "Admin area"


admin_site = MyAdminSite(name='myadmin')
# Register your models here.
admin_site.register(Application)
admin_site.register(Question)
admin_site.register(Answers)
admin_site.register(CoverSheetQuestion)
admin_site.register(CoverSheetAnswers)
admin_site.register(User)
admin_site.register(Group)
