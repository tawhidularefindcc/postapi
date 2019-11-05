from django.db import models

class User(models.Model):
    creating_profile_for = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    contactNo = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)
