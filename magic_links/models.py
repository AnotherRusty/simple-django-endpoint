from django.db import models
from django.contrib.auth.models import User
import secrets
from django.utils import timezone
from datetime import timedelta


def thirty_days_from_now():
    return timezone.now() + timedelta(days=30)


class MagicLink(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.TextField(default=secrets.token_urlsafe)
    expires_at = models.DateTimeField(default=thirty_days_from_now)

    def is_valid(self):
        return timezone.now() < self.expires_at
