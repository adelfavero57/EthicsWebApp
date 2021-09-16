from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import UUIDField
import uuid
# Create your models here.

class Student(models.Model):
    uname = models.CharField(max_length=150, unique=True,
                             primary_key=True, editable=False, null=False)
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.uname
    # You will have to find a way to store a list of applications


class Member(models.Model):
    uname = models.CharField(max_length=150, unique=True,
                             primary_key=True, editable=False, null=False)
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.uname


class Admin(models.Model):
    uname = models.CharField(max_length=150, unique=True,
                             primary_key=True, editable=False, null=False)
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.uname