from django.shortcuts import render, redirect
from .models import Reflection, Submission, Question
from django.utils import timezone,dateformat
from datetime import datetime


def home(request):
    reflections = Reflection.objects.all()
    for reflection in reflections:
        if reflection.date == datetime.utcnow().date():
            questions = Question.objects.filter(reflection=reflection)
            return render(request, "reflections/base.html", {"reflection": reflection,"questions": questions})
        else:
            return render(request, "reflections/base.html", {"reflection": reflection})

def submit_reflection(request,id):
    question = Question.objects.get(id=id)
    return render(request, "reflections/base.html",{"question": question})
