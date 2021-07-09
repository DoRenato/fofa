from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistroForm(UserCreationForm):
    class Meta:
        model= User
        fields= ('username','first_name', 'password1','password2')