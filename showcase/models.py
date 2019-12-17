from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    headline = models.TextField()
    bio = models.TextField()
    codepen = models.URLField(blank=True)
    github_repository = models.URLField(blank=True)

    def __str__(self):
        return self.headline


class StudentOfTheDay(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.PROTECT)
    date = models.DateField()

    @staticmethod
    def get_student_of_the_day():
        today = timezone.now()
        try:
            return StudentOfTheDay.objects.get(date=today)
        except StudentOfTheDay.DoesNotExist:
            return StudentOfTheDay.objects.create(
                date=today, student=Profile.objects.order_by("?").first()
            )

