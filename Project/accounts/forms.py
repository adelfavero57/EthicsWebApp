from django import forms
from django.forms import ModelForm
from .models import NormalUser
from django import forms as forms2


class CreateUserForm(ModelForm):
    class Meta:
        model = NormalUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms2.Form):
    username = forms2.CharField()
    password = forms2.CharField(widget=forms2.PasswordInput)
    remember_me = forms2.BooleanField(required=False)
    custom_error = False
