from django import forms

class Checkinform (forms.ModelForm):
    date_and_time = forms.DateTimeField(required=True)