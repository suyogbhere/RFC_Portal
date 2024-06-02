from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


class Request_Type(models.Model):
    id = models.AutoField(primary_key=True)
    request_name = models.CharField(max_length=100)

    def __str__(self):
        return self.request_name

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Authorizer_Name(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Executor_Name(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class System_Details(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =200)

    def __str__(self):
        return self.name


class RFC_Register(models.Model):
    Rfc_Number = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add= True)
    Reference_RFC_No = models.IntegerField(default=0)
    Department = models.ForeignKey(Department, on_delete = models.CASCADE)
    Request_Type = models.ForeignKey(Request_Type, on_delete = models.CASCADE)
    Environment = models.CharField(max_length=100)
    Planned_Date = models.DateField()
    Category = models.ForeignKey(Category, on_delete = models.CASCADE)
    Reason_for_change = models.CharField(max_length = 200)
    Description_of_change = models.CharField(max_length = 500)
    System_Details = models.ForeignKey(System_Details, on_delete = models.CASCADE)
    To_be_executed_by = models.ForeignKey(Executor_Name, on_delete = models.CASCADE)
    Change_Requested_by = models.CharField(max_length =100)
    Change_authorizer = models.ForeignKey(Authorizer_Name, on_delete = models.CASCADE)
    Change_level = models.CharField(max_length=100)
    Change_impact_assessment = models.CharField(max_length=200)
    Risk_Rating = models.CharField(max_length=100)
    Attachments = models.FileField(upload_to='Attachment')
    Change_rollback_procedures = models.CharField(max_length=200)
    Activity_Notes = models.CharField(max_length=200, null=True,blank=True)
    status = models.CharField(max_length=100, null=True,blank=True)
    Activity_Date = models.DateTimeField(null= True,blank=True)














