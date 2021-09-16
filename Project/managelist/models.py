from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Application(models.Model):

    project_title = models.CharField(max_length=200)

    project_date = models.DateField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    progress = models.IntegerField()

    status = models.CharField(max_length=200)





    

