from accounts.models import Admin, Member, Student
from django.contrib import admin

# Register your models here.
admin.site.register(Student)
admin.site.register(Member)
admin.site.register(Admin)
