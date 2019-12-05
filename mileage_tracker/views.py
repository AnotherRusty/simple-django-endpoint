from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mileage_tracker.forms import MileageForm
from mileage_tracker.models import DistanceToWork

# Create your views here.
@login_required(login_url='login/')
def set_commute(request):
    if request.method == 'POST':
        form = MileageForm(request.POST)
        if form.is_valid():
            miles = form.cleaned_data["miles"]
            DistanceToWork.objects.create(user=request.user, miles=miles)
        return render(request, "home.html")
    else:
        return render(request, 'mileage_tracker/mileage-form.html')