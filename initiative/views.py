from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django import views
from initiative.models import Initiative
from initiative.forms import InitiativeForm
from django.utils import timezone


class InitiativeView(views.View):
    def get(self, request):
        initiatives = Initiative.objects.all()
        return render(
            request,
            "initiative.html",
            {"initiatives": initiatives, "form": InitiativeForm()},
        )


class InitiativeCreateView(LoginRequiredMixin, views.View):
    def post(self, request):
        form = InitiativeForm(request.POST)
        initiatives = Initiative.objects.all()
        if form.is_valid():
            Initiative.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                team_leader=request.user,
                date=timezone.now(),
            )
            return redirect("initiatives:home")
        else:
            return render(
                request, "initiative.html", {"initiatives": initiatives, "form": form}
            )


class InitiativeStatusReportView(LoginRequiredMixin, views.View):
    def edit_post(self, request, id):
        post = Post.objects.get(id=id)
        if request.method == 'POST':
            form = InitiativeForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                url = reverse('initiatives:home', kwargs={'id': id})
                return render(request, 'edit_done.html', {'url': url})
            else:
                form = InitiativeForm(instance=post)
        else:
            form = InitiativeForm(instance=post)
        return render(request, 'edit.html', {'form':form, 'post':post})

    def del_post(request, key):
        post = Initiative.objects.get(id=id)
        post.delete()
        return render(request, 'del_done.html')
