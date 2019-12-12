from django.shortcuts import render, redirect
from .models import Reflection, Submission, Question, QuestionSubmission, User
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
    reflection = Reflection.objects.get(id=id)
    submission = reflection.submission_set.create(user=request.user)
    for key, value in request.POST.items():
        if key.startswith("question-"):
            question_id = int(key.split("-")[1])
            question = Question.objects.get(id=question_id)
            question.questionsubmission_set.create(
                question=question, submission=submission, answer=value
            )
    return redirect("home")
