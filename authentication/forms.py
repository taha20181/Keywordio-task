from django import forms
from django.contrib.auth.forms import UserCreationForm
from lms.models import User

class CreateAdminForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')