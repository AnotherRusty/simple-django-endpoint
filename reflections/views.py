from django.shortcuts import render, redirect
from .models import Reflection, Submission, Question, QuestionSubmission
from django.utils import timezone, dateformat
from datetime import datetime


def home(request):
    try:
        reflection = Reflection.objects.get(date=timezone.now())
    except Reflection.DoesNotExist:
        reflection = None
    return render(request, "reflections/base.html", {"reflection": reflection})


def submit_reflection(request, id):
    # Process form
    #submission = Submission.objects.create(reflection=Reflection, user=User)
    #for submission in submissions:
        #QuestionSubmission.objects.create(question=reflection.question_set(), submission=)
    #return redirect("reflections:home"
