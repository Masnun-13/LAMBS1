from django.shortcuts import render
from .form import UserRegistrationForm, UserInfoForm, UserDeleteForm
from .models import Userinfo
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "User/home.html")

def register(request):
    if(request.method == "POST"):
        form = UserRegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request, "User/home.html")
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, "User/register.html", context)

def login(request):
    return render(request, "User/login.html", context)

@login_required
def logout(request):
    return render(request, "User/logout.html")

@login_required
def profile(request):
    context = {
        'fname': request.user.first_name,
        'lname': request.user.last_name,
        'email': request.user.email,
    }
    return render(request, "User/profile.html", context)

@login_required
def userinfo(request):
    uinfo = Userinfo.objects.all().order_by('user_id', '-user_age')
    context = {'uinfo': uinfo}
    return render(request, "User/userinfo.html", context)

@login_required()
def enteruserinfo(request):
    if(request.method == "POST"):
        form = UserInfoForm(request.POST)
        if(form.is_valid()):
            form.save()
            uinfo = Userinfo.objects.all().order_by('user_id', '-user_age')
            context = {'uinfo': uinfo}
            return render(request, "User/userinfo.html", context)
    else:
        form = UserInfoForm()
    context = {'form': form}
    return render(request, "User/enteruserinfo.html", context)

@login_required()
def deleteuser(request):
    if(request.method == "POST"):
        form = UserDeleteForm(request.POST)
        if(form.is_valid()):
            b = form.instance.user_id
            for c in Userinfo.objects.all():
                if(c.user_id==b):
                    c.delete()
            uinfo = Userinfo.objects.all().order_by('user_id', '-user_age')
            context = {'uinfo': uinfo}
            return render(request, "User/userinfo.html", context)
    else:
        form = UserDeleteForm()
    context = {'form': form}
    return render(request, "User/delete.html", context)