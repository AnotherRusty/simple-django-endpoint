from django import forms

class MileageForm(forms.Form):
    miles = forms.IntegerField()

class CommuteForm(forms.Form):
    commute = forms.Textarea()