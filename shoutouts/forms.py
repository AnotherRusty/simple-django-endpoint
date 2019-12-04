from django.forms import ModelForm
from shoutouts.models import Shoutout


class ShoutoutForm(ModelForm):
    class Meta:
        model = Shoutout
        fields = ["recipient", "content", "datetime", "user"]
