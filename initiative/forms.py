from django import forms
from django.utils import timezone


class InitiativeForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    team_leader = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super(InitiativeForm, self).__init__(*args, **kwargs)
