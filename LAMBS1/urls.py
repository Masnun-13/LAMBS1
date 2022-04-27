"""LAMBS1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from User import views as uviews
from Routine import views as rviews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', uviews.profile, name="profile"),
    path('register/', uviews.register, name='register'),
    path('', uviews.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='User/login.html'),name="login"),
    path('accounts/profile/', uviews.profile),
    path('logout/', auth_views.LogoutView.as_view(template_name='User/logout.html'),name="logout"),
    path('userinfo/', uviews.userinfo, name="userinfo"),
    path('userinfo/enteruserinfo/', uviews.enteruserinfo, name='enteruserinfo'),
    path('userinfo/deleteuser/', uviews.deleteuser, name='deleteuser'),
    path('userinfo/deleteuser/<str:user_id>/', uviews.deleteuser, name='deleteuser'),
    path('userinfo/updateuser/<str:user_id>/', uviews.updateuser, name='updateuser'),
    path('userinfo/updateuser/', uviews.updateuser, name='updateuser'),
    path('routine/', rviews.routine, name="routines"),
    path('activitylist/', rviews.activitylist, name="activities"),
    path('activitylist/enteractivitylist/', rviews.enteractivitylist, name='enteractivitylist'),
    path('activitylist/entermyactivitylist/', rviews.entermyactivitylist, name='entermyactivitylist'),
    path('activitylist/deletefullactivitylist/', rviews.deletefullactivitylist, name='deletefullactivitylist'),
    path('activitylist/deletemyfullactivitylist/', rviews.deletemyfullactivitylist, name='deletemyfullactivitylist'),
    path('activitylist/deleteactivitylist/', rviews.deleteactivitylist, name='deleteactivitylist'),
    path('activitylist/updateactivitylist/', rviews.updateactivitylist, name='updateactivitylist'),
    path('activitylist/deleteactivitylist/<str:alist_actno>/', rviews.deleteactivitylist, name='deleteactivitylist'),
    path('activitylist/updateactivitylist/<str:alist_actno>/', rviews.updateactivitylist, name='updateactivitylist'),
    path('activitylist/createroutine/', rviews.create_routine, name='createroutine'),
    path('activitylist/createmyroutine/', rviews.create_my_routine, name='createmyroutine'),
    path('activitylist/deleteroutine/', rviews.delete_routine, name='deleteroutine'),
    path('activitylist/deletemyroutine/', rviews.delete_my_routine, name='deletemyroutine'),
    path('activitylist/updateroutine/', rviews.update_routine, name='updateroutine'),
    path('activitylist/updatemyroutine/', rviews.update_my_routine, name='updatemyroutine'),
]
