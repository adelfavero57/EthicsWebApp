from django import forms
from django.forms import ModelForm
from .models import NormalUser
from django import forms as forms2


class CreateUserForm(forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = NormalUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms2.Form):
    username = forms2.CharField()
    password = forms2.CharField(widget=forms2.PasswordInput)
    remember_me = forms2.BooleanField(required=False)
    custom_error = False

class UpdateUserForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']