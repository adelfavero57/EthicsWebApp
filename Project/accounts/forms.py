from django.forms import ModelForm
from django import forms as forms2
from django.contrib.auth import forms
from django.contrib.auth.models import User


class UpdateUserForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class CreateUserForm(forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    

class LoginForm(forms2.Form):
    username = forms2.CharField()
    password = forms2.CharField(widget=forms2.PasswordInput)
    remember_me = forms2.BooleanField(required=False)
    custom_error = False

class UpdateUserForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']