from django.shortcuts import render
from .models import Reflection, Submission, Question
from django.utils import timezone
from datetime import datetime


def home(request):
    reflections = Reflection.objects.all()
    for reflection in reflections:
        if reflection.date == timezone.now().date():
            questions = Question.objects.filter
            return render(request, "reflections/base.html", {"reflection": reflection,"questions": questions})
        else:
            return render(request, "reflections/base.html", {"reflection": reflection})



def submit_reflection(request, submit_id):
    pass
