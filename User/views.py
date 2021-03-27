from django.shortcuts import render
from .form import UserRegistrationForm

def home(request):
    return render(request, "User/home.html")

def profile(request):
    context= {
        'name' : '(Name goes here)',
        'email' : '(Email goes here)',
    }
    return render(request, "User/profile.html", context)

def register(request):
    if(request.method == "POST"):
        form = UserRegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
            context = {
                'name': '(Name goes here)',
                'email': '(Email goes here)',
            }
            return render(request, "User/profile.html", context)
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, "User/register.html", context)

def login(request):
    return render(request, "User/login.html")

def logout(request):
    return render(request, "User/logout.html")
