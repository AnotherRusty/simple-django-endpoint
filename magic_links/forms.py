from django import forms
from .models import MagicLink


class NewMagicLinkForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = MagicLink
        fields = []
