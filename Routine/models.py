from django.db import models
import datetime

# Create your models here.
#id is pk

class Routine(models.Model):
    routine_user = models.CharField(max_length=20, db_column="User")
    routine_activity = models.CharField(max_length=50, db_column="Activity")
    routine_actno = models.IntegerField(db_column="Activity Number", default=0)
    routine_time1 = models.TimeField(db_column="Starting Time")
    routine_time2 = models.TimeField(db_column="Ending Time")

    class Meta:
        db_table="Routine"

