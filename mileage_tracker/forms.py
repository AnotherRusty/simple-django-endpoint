from django import forms


class DriveToWorkForm(forms.Form):
    date = forms.DateField()
