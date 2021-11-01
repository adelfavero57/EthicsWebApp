from django.contrib import admin
from accounts.models import Application, Question, Answers, CoverSheetAnswers, CoverSheetQuestion

class MyAdminSite(admin.AdminSite):

    site_header = "Admin area"


admin_site = MyAdminSite(name='myadmin')
# Register your models here.
admin_site.register(Application)
admin_site.register(Question)
admin.site.register(Answers)
admin.site.register(CoverSheetQuestion)
admin.site.register(CoverSheetAnswers)