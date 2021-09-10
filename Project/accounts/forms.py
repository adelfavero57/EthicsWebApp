from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import forms


class CreateUserForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

