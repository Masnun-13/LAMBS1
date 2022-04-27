from django.db import models
import datetime


# Create your models here.

class Userinfo(models.Model):
    user_id=models.CharField(max_length=8, default=18201000, verbose_name='User ID', unique=True)
    user_firstname = models.CharField(max_length=20, db_column="First name",default="John", verbose_name='First Name')
    user_lastname = models.CharField(max_length=20, db_column="Last name", default="Doe", verbose_name='Last Name')
    user_age = models.IntegerField(db_column="Age", default=0, verbose_name='Age')
    user_occupation = models.CharField(max_length=50, db_column="Occupation", default = "None", verbose_name='Occupation')

    class Meta:
        db_table = "User Info"

