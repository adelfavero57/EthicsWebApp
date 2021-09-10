from django.db import models
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class NormalUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)


    # write some methods that retrive data from database / get data from database
    
    



