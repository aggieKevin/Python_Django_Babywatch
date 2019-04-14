import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Household(models.Model):
    CITY_CHOICES=(
        ('HOU','Houston',),
        ('CS','College Station'),
        ('AU','Austin'),
        ('BR','Bryan'),
        ('WA','Waco'),
    )
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    household_name=models.CharField(max_length=100)
    address_line1=models.CharField(max_length=100)
    address_line2=models.CharField(max_length=100,blank=True)
    city=models.CharField(max_length=30,choices=CITY_CHOICES)
    state=models.CharField(max_length=20)
    zip=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    def __str__(self):
        return self.household_name
    def getCity(self):
        return (self.city).lower()

class Guardian(models.Model):
    GENDER_CHOICES=(
        ('M','Male',),
        ('F','Female'),
    )
    household=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50,blank=True)
    birth_date=models.DateField()
    phone_number=models.CharField(max_length=20)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    driver_license=models.CharField(max_length=30)
    job_type=models.CharField(max_length=30,blank=True)
    company=models.CharField(max_length=30,blank=True)
    relationship=models.CharField(max_length=30)
    def __str__(self):
        return self.first_name+' '+self.last_name

class Child(models.Model):
    GENDER_CHOICES=(
        ('M','Male',),
        ('F','Female'),
    )
    FREE_DAY=(
        ('M','Monday'),
        ('T','Tuesday'),
        ('W','Wednesday'),
        ('R','Thursday'),
        ('F','Friday'),
        ('Sat','Saturday'),
        ('Sun','Sunday'),
    )
    household=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birth_date=models.DateField()
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    hobby=models.CharField(max_length=50,blank=True)
    allergy=models.CharField(max_length=50,blank=True)
    free_day=models.CharField(max_length=3,choices=FREE_DAY)
    def __str__(self):
        return self.first_name +' '+self.last_name

class Rating(models.Model):
    RATING_CHOICES=(
        (5,'Excellent'),
        (4,'Very Good'),
        (3,'Good'),
        (2,'Fair'),
        (1,'Bad')
    )
    receiver=models.ForeignKey(Household,on_delete=models.CASCADE)
    rate=models.IntegerField(choices=RATING_CHOICES,default=5)
    comment=models.CharField(max_length=200,blank=True)
    giver=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.receiver.household_name