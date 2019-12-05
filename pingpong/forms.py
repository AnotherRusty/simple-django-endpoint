from django import forms

class MatchForm(forms.Form):
    player1 = forms.IntegerField()
    player2 = forms.IntegerField()
    player1_score = forms.IntegerField()
    player2_score = forms.IntegerField()