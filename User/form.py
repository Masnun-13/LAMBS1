from django.contrib.auth.forms import UserCreationForm, forms
from django import forms as forms2
from django.contrib.auth.models import User
from User.models import Userinfo

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2'
                  ]

class UserInfoForm(forms2.ModelForm):

    class Meta:
        model = Userinfo
        fields = ['user_id',
                  'user_firstname',
                  'user_lastname',
                  'user_age',
                  'user_occupation'
                  ]

class UserDeleteForm(forms2.ModelForm):

    class Meta:
        model = Userinfo
        fields = ['user_id',
                  ]




