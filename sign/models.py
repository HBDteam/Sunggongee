from django.db import models

# Create your models here.
class User(models.Model):
    studentID = models.CharField(max_length = 8, primary_key = True)
    password = models.BinaryField(max_length = 16, null = False)
    name = models.CharField(max_length = 10, null = False )
    email = mpdelsEmailField(null = False)
    phoneNum = models.CharField(max_length = 11, null = False)
    isEnrolled = models.BooleanField(default = 0, null = False)

class Manager(models.Model):
    mID =  models.CharField(max_length = 8, primary_key = True)
    mPassword = models.BinaryField(max_length = 16, null = False)