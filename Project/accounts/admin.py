from django.contrib import admin
from accounts.models import Application, Question, Answers, CoverSheetAnswers, CoverSheetQuestion

# Register your models here.
admin.site.register(Application)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(CoverSheetQuestion)
admin.site.register(CoverSheetAnswers)
