from django.forms import ModelForm
from .models import USER

class Register(ModelForm):
    class Meta:
        model = USER
        fields = ['username', 'password']


