from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)

class User(AbstractUser):
    usertype=models.CharField(max_length=50)
    phone=models.BigIntegerField()

class Stud_User(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=15)
    plus_mark=models.IntegerField()

class Employee(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=20)


