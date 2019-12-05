from django.shortcuts import render
from .models import Reflection,Submission,Question

def home(request):
    reflections = Reflection.objects.all()
    questions = Question.objects.all()
    return render(request, "reflections/base.html", {"reflections": reflections, "questions":questions})

def submit_reflection(request,submit_id):
    reflection = Reflection.objects.get(id=submit_id)
    Submission.objects.create(
        reflection=reflection , user=request.user
    )
    return render(request, "reflections/base.html")