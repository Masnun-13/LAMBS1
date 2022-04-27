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
    return render(request, "User/login.html")

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
def deleteuser(request, user_id):
    user = Userinfo.objects.get(user_id=user_id)
    form = UserDeleteForm(request.POST)
    if request.method == "POST":
        user.delete()
        uinfo = Userinfo.objects.all().order_by('user_id', '-user_age')
        context = {'uinfo': uinfo}
        return render(request, "User/userinfo.html", context)

    context = {'form': form}
    return render(request, "User/delete.html", context)

@login_required()
def updateuser(request, user_id):
    user = Userinfo.objects.get(user_id=user_id)
    form = UserInfoForm(request.POST)
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            uinfo = Userinfo.objects.all().order_by('user_id', '-user_age')
            context = {'uinfo': uinfo}
            return render(request, "User/userinfo.html", context)
    form = UserInfoForm(initial=user.__dict__)
    context = {'form': form, 'user' : user}
    return render(request, "User/update.html", context)