from django.db import models

# Create your models here.

class Routine(models.Model):
    routine_user = models.CharField(max_length=20, db_column="User")
    routine_time = models.IntegerField(db_column="Time")
    routine_activity = models.CharField(max_length=50, db_column="Activity")

    class Meta:
        db_table="Routine"

