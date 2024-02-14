from django.contrib import admin
from myapp.models import Employee

# Register your models here.

# admin.site.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name')


admin.site.register(Employee,EmployeeAdmin)