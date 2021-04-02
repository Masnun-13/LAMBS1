from django.shortcuts import render
from .models import Routine
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "User/home.html")

@login_required
def routine(request):
    routines = Routine.objects.all()
    context = {'routines': routines}
    return render(request, "Routine/routine.html", context)

