from django.db import models

# Create your models here.


class Student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    dob=models.DateField()
    age=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    dep=(
        ('CS','Computer Science'),
        ('IT','Information Technology')
    )
    deprt=models.CharField(max_length=2,choices=dep)