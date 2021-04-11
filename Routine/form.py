
from django import forms as forms2
from Routine.models import Routine, Activitylist

class ActivitylistForm(forms2.ModelForm):

    class Meta:
        model = Activitylist
        fields = ['alist_username',
                  'alist_activity',
                  'alist_actno',
                  'alist_time',
                  'alist_day'
                  ]

class ShortAlistForm(forms2.ModelForm):

    class Meta:
        model = Activitylist
        fields = ['alist_username',
                  'alist_day'
                  ]




