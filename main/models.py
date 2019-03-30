import datetime
from django.db import models
from django.utils import timezone

class Household(models.Model):
    address_line1=models.CharField(max_length=100)
    address_line2=models.CharField(max_length=100,blank=True)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=20)
    zip=models.CharField(max_length=20)
    email=models.CharField(max_length=50)

class Guardian(models.Model):
    GENDER_CHOICES=(
        ('M','Male',),
        ('F','Female'),
    )
    household=models.ForeignKey(Household,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50,blank=True)
    birth_date=models.DateField()
    phone_number=models.CharField(max_length=20)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    drive_license=models.CharField(max_length=30)
    job_type=models.CharField(max_length=30,blank=True)
    company=models.CharField(max_length=30,blank=True)
    relationship=models.CharField(max_length=30)

class Child(models.Model):
    GENDER_CHOICES=(
        ('M','Male',),
        ('F','Female'),
    )
    household=models.ForeignKey(Household,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birth_date=models.DateField()
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    hobby=models.CharField(max_length=50,blank=True)
    allergy=models.CharField(max_length=50,blank=True)
    free_date=models.DateField()

'''
class Rating(models.Model):
    RATING_CHOICES=(
        (5,'Excellent'),
        (4,'Very Good'),
        (3,'Good'),
        (2,'Fair'),
        (1,'Bad')
    )
'''