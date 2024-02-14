from django.db import models

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    dob=models.DateField()
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)

    class Meta:
        db_table="tblstude"

class Employee(models.Model):
    first_name=models.CharField(max_length=15,verbose_name="Enter Your name")
    last_name=models.CharField(max_length=15)
    dob=models.DateField()
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    deprt=(
        ('HR','Human Resource'),
        ('CS','Computer Science'),
        ('EC','Electronic And Communications')
    )
    deprt=models.CharField(max_length=2,choices=deprt)