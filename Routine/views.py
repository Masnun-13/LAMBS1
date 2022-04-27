from django.shortcuts import render
from .models import Routine, Activitylist
from django.contrib.auth.decorators import login_required
from .form import ActivitylistForm, ShortAlistForm, ActivitylistForm2, ShortAlistForm2
import datetime


def home(request):
    return render(request, "User/home.html")


@login_required
def routine(request):
    if (request.method == "POST"):
        routines = Routine.objects.filter(routine_user=(request.POST.get('userdrop'))).order_by('routine_user',
                                                                                                'routine_day',
                                                                                                'routine_time1')
        users = Routine.objects.order_by().values('routine_user').distinct()
        context = {'routines': routines,
                   'users': users}
        return render(request, "Routine/routine.html", context)
    else:
        routines = Routine.objects.all().order_by('routine_user', 'routine_time1')
        users = Routine.objects.order_by().values('routine_user').distinct()
        context = {'routines': routines,
                   'users': users}
        return render(request, "Routine/routine.html", context)


@login_required
def activitylist(request):
    activities = Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno')
    context = {'activities': activities}
    return render(request, "Routine/activitylist.html", context)


@login_required()
def enteractivitylist(request):
    if (request.method == "POST"):
        form = ActivitylistForm(request.POST)
        if (form.is_valid()):
            form.save()
            activities = Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno')
            context = {'activities': activities}
            return render(request, "Routine/activitylist.html", context)
    else:
        form = ActivitylistForm()
    context = {'form': form}
    return render(request, "Routine/enteractivitylist.html", context)


def entermyactivitylist(request):
    if (request.method == "POST"):
        form = ActivitylistForm2(request.POST)
        if (form.is_valid()):
            form2 = form.save(commit=False)
            form2.alist_username = (str)(request.user)
            form2.save()
            form.save()
            activities = Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno')
            context = {'activities': activities}
            return render(request, "Routine/activitylist.html", context)
    else:
        form = ActivitylistForm2
    context = {'form': form}
    return render(request, "Routine/enteractivitylist.html", context)


@login_required()
def deleteactivitylist(request, alist_actno):
    activity = Activitylist.objects.get(alist_actno=alist_actno)
    form = ShortAlistForm(request.POST)
    if request.method == "POST":
        activity.delete()
        activities = Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno')
        context = {'activities': activities}
        return render(request, "Routine/activitylist.html", context)

    context = {'form': form}
    return render(request, "Routine/deleteactivitylist.html", context)


@login_required()
def updateactivitylist(request, alist_actno):
    activity = Activitylist.objects.get(alist_actno=alist_actno)
    form = ActivitylistForm(request.POST)
    if request.method == 'POST':
        form = ActivitylistForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            activities = Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno')
            context = {'activities': activities}
            return render(request, "Routine/activitylist.html", context)

    form = ActivitylistForm(initial=activity.__dict__)
    context = {'form': form}
    return render(request, "Routine/updateactivitylist.html", context)


@login_required()
def deletefullactivitylist(request):
    if (request.method == "POST"):
        form = ShortAlistForm(request.POST)
        if (form.is_valid()):
            a = form.instance.alist_day
            b = form.instance.alist_username
            for c in Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno'):
                if (c.alist_day == a and c.alist_username == b):
                    c.delete()
            activities = Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno')
            context = {'activities': activities}
            return render(request, "Routine/activitylist.html", context)
    else:
        form = ShortAlistForm()
    context = {'form': form}
    return render(request, "Routine/deletefullactivitylist.html", context)


@login_required()
def deletemyfullactivitylist(request):
    if (request.method == "POST"):
        form = ShortAlistForm2(request.POST)
        if (form.is_valid()):
            a = form.instance.alist_day
            b = (str)(request.user)
            for c in Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno'):
                if (c.alist_day == a and c.alist_username == b):
                    c.delete()
            activities = Activitylist.objects.all().order_by('alist_username', 'alist_day', 'alist_actno')
            context = {'activities': activities}
            return render(request, "Routine/activitylist.html", context)
    else:
        form = ShortAlistForm2()
    context = {'form': form}
    return render(request, "Routine/deletefullactivitylist.html", context)


@login_required
def create_routine(request):
    if (request.method == "POST"):
        form = ShortAlistForm(request.POST)
        if (form.is_valid()):
            f = 0
            a = form.instance.alist_day
            b = form.instance.alist_username
            for x in Activitylist.objects.all().order_by('-alist_priority'):
                f = x.alist_stime
                g = x.alist_stime + x.alist_time - 1
                if (x.alist_username == b and x.alist_day == a):
                    for t in range(f, g):
                        if (Routine.objects.filter(routine_time1=datetime.time(t, 0, 0)).filter(routine_user=b).filter(
                                routine_day=a).exists()):
                            r = Routine(routine_user=b, routine_day=a, routine_activity=x.alist_activity,
                                        routine_actno=x.alist_actno,
                                        routine_time1=datetime.time(f, 0, 0),
                                        routine_time2=datetime.time(t - 1, 59, 59))

                            r.save()
                            f = t
                        else:
                            if (Routine.objects.filter(routine_time2=datetime.time(t, 59, 59)).filter(
                                    routine_user=b).filter(
                                    routine_day=a).exists()):
                                f = t + 1
                            else:
                                continue

                    r = Routine(routine_user=b, routine_day=a, routine_activity=x.alist_activity,
                                routine_actno=x.alist_actno,
                                routine_time1=datetime.time(f, 0, 0),
                                routine_time2=datetime.time(g, 59, 59))
                    r.save()
            routines = Routine.objects.filter(routine_user=b).order_by('routine_user', 'routine_day', 'routine_time1')
            users = Routine.objects.order_by().values('routine_user').distinct()
            context = {'routines': routines,
                       'users': users}
            return render(request, "Routine/routine.html", context)
    else:
        form = ShortAlistForm()
    context = {'form': form}
    return render(request, "Routine/createroutine.html", context)


def create_my_routine(request):
    if (request.method == "POST"):
        form = ShortAlistForm2(request.POST)
        if (form.is_valid()):
            f = 0
            a = form.instance.alist_day
            b = (str)(request.user)

            for x in Activitylist.objects.all().order_by('-alist_priority'):
                f = x.alist_stime
                g = x.alist_stime + x.alist_time - 1
                if (x.alist_username == b and x.alist_day == a):
                    for t in range(f, g):
                        if (Routine.objects.filter(routine_time1=datetime.time(t, 0, 0)).filter(routine_user=b).filter(
                                routine_day=a).exists()):
                            r = Routine(routine_user=b, routine_day=a, routine_activity=x.alist_activity,
                                        routine_actno=x.alist_actno,
                                        routine_time1=datetime.time(f, 0, 0),
                                        routine_time2=datetime.time(t - 1, 59, 59))

                            r.save()
                            f = t
                        else:
                            if(Routine.objects.filter(routine_time2=datetime.time(t, 59, 59)).filter(routine_user=b).filter(
                                    routine_day=a).exists()):
                                f = t+1
                            else:
                                continue

                    r = Routine(routine_user=b, routine_day=a, routine_activity=x.alist_activity,
                                routine_actno=x.alist_actno,
                                routine_time1=datetime.time(f, 0, 0),
                                routine_time2=datetime.time(g, 59, 59))
                    r.save()
            routines = Routine.objects.filter(routine_user=b).order_by('routine_user', 'routine_day', 'routine_time1')
            users = Routine.objects.order_by().values('routine_user').distinct()
            context = {'routines': routines,
                       'users': users}
            return render(request, "Routine/routine.html", context)
    else:
        form = ShortAlistForm2()
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
            users = Routine.objects.order_by().values('routine_user').distinct()
            context = {'routines': routines,
                       'users': users}
            return render(request, "Routine/routine.html", context)
    else:
        form = ShortAlistForm()
    context = {'form': form}
    return render(request, "Routine/deleteroutine.html", context)


@login_required
def delete_my_routine(request):
    if (request.method == "POST"):
        form = ShortAlistForm2(request.POST)
        if (form.is_valid()):
            a = form.instance.alist_day
            b = (str)(request.user)
            for c in Routine.objects.all():
                if (c.routine_day == a and c.routine_user == b):
                    c.delete()
            routines = Routine.objects.all().order_by('routine_user', 'routine_day', 'routine_time1')
            users = Routine.objects.order_by().values('routine_user').distinct()
            context = {'routines': routines,
                       'users': users}
            return render(request, "Routine/routine.html", context)
    else:
        form = ShortAlistForm2()
    context = {'form': form}
    return render(request, "Routine/deleteroutine.html", context)


@login_required
def update_routine(request):
    if (request.method == "POST"):
        form = ShortAlistForm(request.POST)
        if (form.is_valid()):
            f = 0
            a = form.instance.alist_day
            b = form.instance.alist_username
            for c in Routine.objects.all():
                if (c.routine_day == a and c.routine_user == b):
                    c.delete()
            for x in Activitylist.objects.all().order_by('-alist_priority'):
                f = x.alist_stime
                g = x.alist_stime + x.alist_time - 1
                if (x.alist_username == b and x.alist_day == a):
                    for t in range(f, g):
                        if (Routine.objects.filter(routine_time1=datetime.time(t, 0, 0)).filter(routine_user=b).filter(
                                routine_day=a).exists()):
                            r = Routine(routine_user=b, routine_day=a, routine_activity=x.alist_activity,
                                        routine_actno=x.alist_actno,
                                        routine_time1=datetime.time(f, 0, 0),
                                        routine_time2=datetime.time(t - 1, 59, 59))

                            r.save()
                            f = t
                        else:
                            if (Routine.objects.filter(routine_time2=datetime.time(t, 59, 59)).filter(
                                    routine_user=b).filter(
                                    routine_day=a).exists()):
                                f = t + 1
                            else:
                                continue

                    r = Routine(routine_user=b, routine_day=a, routine_activity=x.alist_activity,
                                routine_actno=x.alist_actno,
                                routine_time1=datetime.time(f, 0, 0),
                                routine_time2=datetime.time(g, 59, 59))
                    r.save()
            routines = Routine.objects.filter(routine_user=b).order_by('routine_user', 'routine_day', 'routine_time1')
            users = Routine.objects.order_by().values('routine_user').distinct()
            context = {'routines': routines,
                       'users': users}
            return render(request, "Routine/routine.html", context)
    else:
        form = ShortAlistForm2()
    context = {'form': form}
    return render(request, "Routine/updateroutine.html", context)


@login_required
def update_my_routine(request):
    if (request.method == "POST"):
        form = ShortAlistForm2(request.POST)
        if (form.is_valid()):
            f = 0
            a = form.instance.alist_day
            b = (str)(request.user)
            for c in Routine.objects.all():
                if (c.routine_day == a and c.routine_user == b):
                    c.delete()
            for x in Activitylist.objects.all().order_by('-alist_priority'):
                f = x.alist_stime
                g = x.alist_stime + x.alist_time - 1
                if (x.alist_username == b and x.alist_day == a):
                    for t in range(f, g):
                        if (Routine.objects.filter(routine_time1=datetime.time(t, 0, 0)).filter(routine_user=b).filter(
                                routine_day=a).exists()):
                            r = Routine(routine_user=b, routine_day=a, routine_activity=x.alist_activity,
                                        routine_actno=x.alist_actno,
                                        routine_time1=datetime.time(f, 0, 0),
                                        routine_time2=datetime.time(t - 1, 59, 59))

                            r.save()
                            f = t
                        else:
                            if (Routine.objects.filter(routine_time2=datetime.time(t, 59, 59)).filter(
                                    routine_user=b).filter(
                                    routine_day=a).exists()):
                                f = t + 1
                            else:
                                continue

                    r = Routine(routine_user=b, routine_day=a, routine_activity=x.alist_activity,
                                routine_actno=x.alist_actno,
                                routine_time1=datetime.time(f, 0, 0),
                                routine_time2=datetime.time(g, 59, 59))
                    r.save()
            routines = Routine.objects.filter(routine_user=b).order_by('routine_user', 'routine_day', 'routine_time1')
            users = Routine.objects.order_by().values('routine_user').distinct()
            context = {'routines': routines,
                       'users': users}
            return render(request, "Routine/routine.html", context)
    else:
        form = ShortAlistForm2()
    context = {'form': form}
    return render(request, "Routine/updateroutine.html", context)