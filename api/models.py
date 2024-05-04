from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(('IT','IT'),('NON IT','NON IT'),('MOBILE Company','MOBILE Company')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(('IT','IT'),('NON IT','NON IT'),('MOBILE Company','MOBILE Company')))
    hire_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
