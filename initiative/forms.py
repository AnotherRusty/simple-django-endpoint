from django import forms

class InitiativeForm(forms.Form):
    name = forms.CharField()
    team_leader = forms.CharField()
    goal_date = forms.DateField()
    team = forms.CharField()
    timeline = forms.CharField()