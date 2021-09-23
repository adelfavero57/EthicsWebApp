from django.contrib import admin
from accounts.models import Application, Question, Answers

# Register your models here.
admin.site.register(Application)
admin.site.register(Question)
admin.site.register(Answers)