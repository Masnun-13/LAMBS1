from django.db import models

# Create your models here.

class Userinfo(models.Model):
    user_name = models.CharField(max_length=20, db_column="Username")
    user_age = models.IntegerField(db_column="Age")
    user_occupation = models.CharField(max_length=50, db_column="Occupation")

    class Meta:
        db_table = "User Info"

