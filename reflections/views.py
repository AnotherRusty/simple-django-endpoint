from django.shortcuts import render, redirect
from .models import Reflection, Submission, Question, QuestionSubmission, User
from django.utils import timezone, dateformat
from datetime import datetime
from django.contrib.auth.models import User


def home(request):
    user = request.user
    try:
        reflection = Reflection.objects.get(date=timezone.now())
        submission = reflection.submission_set.get(user=user)
    except Reflection.DoesNotExist:
        reflection = None
        submission = None
    except Submission.DoesNotExist:
        submission = None

    return render(request, "reflections/base.html", {"reflection": reflection, "submission": submission})


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
    return redirect("reflections:home")


def admin_view(request):
    users = User.objects.all()
    submissions = Submission.objects.all()
    try:
        reflection = Reflection.objects.get(date=timezone.now())
    except Reflection.DoesNotExist:
        reflection = None
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
def individual_feedback(request,id):
    feedback = request.POST["individual_feedback"]
    reflection = Reflection.objects.get(date=timezone.now())
    submission = Submission.objects.get(id=id)
    submission.feedback = feedback
    submission.save()
    return redirect("reflections:home")
    