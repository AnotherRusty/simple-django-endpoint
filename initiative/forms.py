from django import forms
from django.utils import timezone
from django.contrib.auth.models import User


class InitiativeForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()