from django.shortcuts import render, redirect
from django.views import View

class Attendance(View):
    def get(self, request):
        return render(request, "attendance.html")
