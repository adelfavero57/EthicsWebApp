from django.db import models

# Create your models here.

class Application(models.Model):

    project_name = models.CharField(max_length=200)
    