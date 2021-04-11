from django.shortcuts import render
from .models import Routine, Activitylist
from django.contrib.auth.decorators import login_required
from .form import ActivitylistForm, ShortAlistForm
import datetime

def home(request):
    return render(request, "User/home.html")

@login_required
def routine(request):
    routines = Routine.objects.all().order_by('routine_user', 'routine_day', 'routine_time1')
    context = {'routines': routines}
    return render(request, "Routine/routine.html", context)

@login_required
def activitylist(request):
    activities = Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno')
    context = {'activities': activities}
    return render(request, "Routine/activitylist.html", context)

@login_required()
def enteractivitylist(request):
    if(request.method == "POST"):
        form = ActivitylistForm(request.POST)
        if(form.is_valid()):
            form.save()
            activities = Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno')
            context = {'activities': activities}
            return render(request, "Routine/activitylist.html", context)
    else:
        form = ActivitylistForm()
    context = {'form': form}
    return render(request, "Routine/enteractivitylist.html", context)

@login_required()
def deleteactivitylist(request):
    if(request.method == "POST"):
        form = ShortAlistForm(request.POST)
        if(form.is_valid()):
            a = form.instance.alist_day
            b = form.instance.alist_username
            for c in Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno'):
                if(c.alist_day==a and c.alist_username==b):
                    c.delete()
            activities = Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno')
            context = {'activities': activities}
            return render(request, "Routine/activitylist.html", context)
    else:
        form = ShortAlistForm()
    context = {'form': form}
    return render(request, "Routine/deleteactivitylist.html", context)

@login_required
def create_routine(request):
    if (request.method == "POST"):
        form = ShortAlistForm(request.POST)
        if (form.is_valid()):
            f=0
            a = form.instance.alist_day
            b = form.instance.alist_username
            for x in Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno'):
                if(x.alist_username==b and x.alist_day==a):
                    for t in range(f, f+x.alist_time):
                        r = Routine(routine_user=b, routine_day=a, routine_activity=x.alist_activity, routine_actno=x.alist_actno,
                                    routine_time1=datetime.time(t, 0, 0), routine_time2=datetime.time(t, 59, 59))
                        r.save()
                    f=f+x.alist_time
            if(f<24):
                for t in range(f, 24):
                    r = Routine(routine_user=b, routine_day=a, routine_activity="Free Time", routine_actno=0,
                                routine_time1=datetime.time(t, 0, 0), routine_time2=datetime.time(t, 59, 59))
                    r.save()
            routines = Routine.objects.all().order_by('routine_user', 'routine_day', 'routine_time1')
            context = {'routines': routines}
            return render(request, "Routine/routine.html", context)
    else:
        form = ShortAlistForm()
    context = {'form': form}
    return render(request, "Routine/createroutine.html", context)

@login_required
def delete_routine(request):
    if (request.method == "POST"):
        form = ShortAlistForm(request.POST)
        if (form.is_valid()):
            a = form.instance.alist_day
            b = form.instance.alist_username
            for c in Routine.objects.all():
                if (c.routine_day == a and c.routine_user == b):
                    c.delete()
            routines = Routine.objects.all().order_by('routine_user', 'routine_day', 'routine_time1')
            context = {'routines': routines}
            return render(request, "Routine/routine.html", context)
    else:
        form = ShortAlistForm()
    context = {'form': form}
    return render(request, "Routine/deleteroutine.html", context)