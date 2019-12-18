from django.shortcuts import render, redirect
from .models import Reflection, Submission, Question, QuestionSubmission, User,Feedback
from django.utils import timezone, dateformat
from datetime import datetime
from django.contrib.auth.models import User


def home(request):
    try:
        reflection = Reflection.objects.get(date=timezone.now())
    except Reflection.DoesNotExist:
        reflection = None
    try:
        feedback_class = Feedback.objects.get(reflection=reflection)
    except Feedback.DoesNotExist:
        feedback_class = None
    return render(request, "reflections/base.html", {"reflection": reflection, "feedback_class": feedback_class})


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


def admin_view(request):
    users = User.objects.all()
    submissions = Submission.objects.all()
    try:
        reflection = Reflection.objects.get(date=timezone.now())
        reflection_date = reflection.date
    except Reflection.DoesNotExist:
        reflection = None
    for user in users:
        if user.submission_set.filter(reflection=reflection).exists():
            done = "Yes"

        else:
            done = "No"

    return render(
        request,
        "reflections/admin_view.html",
        {"users": users, "reflection": reflection, "submissions": submissions},
    )


def submission_detail(request):
    reflection = Reflection.objects.get(date=timezone.now())
    submission = Submission.objects.get(user=request.user, reflection=reflection)
    return render(
        request,
        "reflections/submission_detail.html",
        {"reflection": reflection, "submission": submission},
    )