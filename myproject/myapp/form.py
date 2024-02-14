from django import forms
from myapp.models import Employee

class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        # fields="__all__"
        # fields=["first_name","last_name","dob"]
        exclude=["last_name"]

class studform(forms.Form):
    first_name=forms.CharField(label="Enter your name : ",max_length=10)
    email=forms.CharField(label="Enter email : ",max_length=20)
    