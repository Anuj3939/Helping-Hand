from django.db import models
import datetime
import os


default_auto_field = 'django.db.models.BigAutoField'
class Cycle(models.Model):
     Name=models.CharField(max_length=50)
     Registration_num=models.CharField(max_length=7)
     Roll_num=models.IntegerField()
     Hostel=models.CharField(max_length=30)
     Room_number=models.CharField(max_length=6)
     Phone_num=models.CharField(max_length=15)
     Course=models.CharField(max_length=8)
     Photo=models.ImageField(upload_to="upload_images")

class Cooler(models.Model):
     Name = models.CharField(max_length=50)
     Registration_num = models.CharField(max_length=7)
     Roll_num = models.IntegerField()
     Hostel = models.CharField(max_length=30)
     Room_number = models.CharField(max_length=6)
     Phone_num = models.CharField(max_length=15)
     Course = models.CharField(max_length=8)
     Photo = models.ImageField(upload_to="cooler_images")

class FoodPlace(models.Model):
     Name=models.TextField()
     address=models.TextField()
     foodtype=models.TextField()
     photo=models.ImageField(upload_to="food_images")

class Visit_place(models.Model):
     Name=models.CharField(max_length=50)
     Address=models.CharField(max_length=30)
     Distance=models.CharField(max_length=7)
     Mode=models.CharField(max_length=15)
     Photo=models.ImageField(upload_to="place_images")


# Create your models here.
