from django import forms
from django.utils import timezone
from django.contrib.auth.models import User


class InitiativeForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()


class InitiativeUpdateForm(forms.ModelForm):
    class Meta:
        model = InitiativeForm
        title = forms.CharField(widget=forms.TextInput())
        fields = ["team_leader", "title", "description"]

