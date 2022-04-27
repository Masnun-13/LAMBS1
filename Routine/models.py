from django.db import models
import datetime

# Create your models here.
#id is pk

class Routine(models.Model):
    routine_user = models.CharField(max_length=20, db_column="User", verbose_name='User')
    routine_activity = models.CharField(max_length=50, db_column="Activity", verbose_name='Activity')
    routine_actno = models.IntegerField(db_column="Activity Number", default=0, verbose_name='Activity Number')
    routine_time1 = models.TimeField(db_column="Starting Time", verbose_name='Starting Time')
    routine_time2 = models.TimeField(db_column="Ending Time", verbose_name='Ending Time')
    routine_day = models.CharField(db_column="Day", max_length=10, default="Sunday", verbose_name='Day of Week')

    class Meta:
        db_table="Routine"


class Activitylist(models.Model):
    alist_username = models.CharField(max_length=20, db_column="User", verbose_name='User')
    alist_activity = models.CharField(max_length=50, db_column="Activity", verbose_name='Activity')
    alist_actno = models.IntegerField(db_column="Activity Number", default=0, verbose_name='Activity Number')
    alist_priority = models.IntegerField(db_column="Activity Priority", default=0, verbose_name='Activity Priority')
    alist_stime = models.IntegerField(db_column="Starting time", default=0, verbose_name='Starting time')
    alist_time = models.IntegerField(db_column="Time Spent (Hours)", default=0, verbose_name='Time Spent (Hours)')
    alist_day = models.CharField(db_column="Day", max_length=10, default="Sunday", verbose_name='Day of Week')

    class Meta:
        db_table="Activity List"

