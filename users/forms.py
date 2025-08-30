# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'password1', 'password2']
