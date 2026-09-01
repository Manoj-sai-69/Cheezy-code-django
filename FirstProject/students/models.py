from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    reg_no=models.CharField(max_length=9)
    section=models.CharField(max_length=1)
    mobile=models.CharField(RegexValidator(regex=r'^[6-9]\d{9}$',message="please enter a valid phone number"))
