from django.shortcuts import render
from .form import UserRegistrationForm
from .models import Userinfo
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "User/home.html")

def register(request):
    if(request.method == "POST"):
        form = UserRegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
            context = {
                'fname': request.user.first_name,
                'lname': request.user.last_name,
                'email': request.user.email,
            }
            return render(request, "User/profile.html", context)
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
    uinfo = Userinfo.objects.all()
    context = {'uinfo': uinfo}
    return render(request, "User/userinfo.html", context)

