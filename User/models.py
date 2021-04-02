from django.db import models
import datetime


# Create your models here.

class Userinfo(models.Model):
    user_firstname = models.CharField(max_length=20, db_column="First name",default="John")
    user_lastname = models.CharField(max_length=20, db_column="Last name", default="Doe")
    user_age = models.IntegerField(db_column="Age", default=0)
    user_occupation = models.CharField(max_length=50, db_column="Occupation", default = "None")

    class Meta:
        db_table = "User Info"

