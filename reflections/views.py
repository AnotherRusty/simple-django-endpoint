from django.shortcuts import render, redirect
from .models import Reflection, Submission, Question, QuestionSubmission, User
from django.utils import timezone, dateformat
from datetime import datetime
from django.contrib.auth.models import User


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


def admin_view(request):
    users = User.objects.all()
    submissions = Submission.objects.all()
    try:
        reflection = Reflection.objects.get(date=timezone.now())
        reflection_date = reflection.date
    except Reflection.DoesNotExist:
        reflection = None
    correction_list = []
    for user in users:
        if user.submission_set.filter(reflection=reflection).exists():
            done = "Yes"
            correction_list.append(done)
        else:
            done = "No"
            correction_list.append(done)
    return render(
        request,
        "reflections/admin_view.html",
        {
            "users": users,
            "reflection": reflection,
            "submissions": submissions,
            "correction_list": correction_list,
        },
    )


def submission_detail(request, id):
    try:
        reflection = Reflection.objects.get(date=timezone.now())
    except Reflection.DoesNotExist:
        reflection = None
    user = User.objects.get(id=id)
    submission = Submission.objects.get(user=user, reflection=reflection)
    return render(
        request,
        "reflections/submission_detail.html",
        {"reflection": reflection, "user": user, "submission": submission},
    )

