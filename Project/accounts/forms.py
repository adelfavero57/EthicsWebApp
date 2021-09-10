from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import forms
from django import forms as forms2
from django.utils.translation import ugettext, ugettext_lazy as _


class CreateUserForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class LoginForm(forms2.Form):
    username = forms2.CharField()
    password = forms2.CharField(widget=forms2.PasswordInput)
    remember_me = forms2.BooleanField(required=False)
    custom_error = False
