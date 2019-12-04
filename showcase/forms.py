from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login



class SignUp(forms.ModelForm):
    email = forms.EmailField()