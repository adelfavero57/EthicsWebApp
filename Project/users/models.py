from django.db import models

# Create your models here.

class USER(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    def get_password(self):
        return self.password
