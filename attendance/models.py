from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from attendance.choices import *


class Checkin(models.Model):
    EIGHT_THIRTY = timezone.now().replace(hour=8, minute=30)

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
    verified = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)

    @staticmethod
    def checkin_user(user):
        return user.checkin_set.create()

    @staticmethod
    def is_user_checked_in(user):
        return user.checkin_set.filter(datetime__date=timezone.now().date()).exists()

    @staticmethod
    def daily_report():
        report = {}
        users = User.objects.all()
        for user in users:
            if user.checkin_set.filter(datetime__date=timezone.now()).exists():
                checkin = user.checkin_set.filter(datetime__date=timezone.now()).first()
                report[user] = checkin.compute_status()
            else:
                report[user] = "Absent"
        return report

    def compute_status(self):
        if self.datetime < Checkin.EIGHT_THIRTY:
            return "Present"
        else:
            return "Tardy"
    