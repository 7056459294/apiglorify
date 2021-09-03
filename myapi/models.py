from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=60, default="")
    phone_no= models.CharField(max_length=12, default="")
    email = models.CharField(max_length=70, default="")
    password=models.CharField(max_length=20,default="")
    def __str__(self):
        return self.username


class guser(models.Model):
    full_name = models.CharField(max_length=60, default="")
    email = models.CharField(max_length=70, default="")
    phone_no= models.CharField(max_length=12, default="")
    password=models.CharField(max_length=20,default="")
    def __str__(self):
        return self.full_name

class hotel(models.Model):
    hotel_name=models.CharField(max_length=200, default="")
    desc=models.CharField(max_length=200, default="")
    city=models.CharField(max_length=200, default="")
    address=models.CharField(max_length=300, default="")
    price=models.IntegerField()
    faculties= models.JSONField()
    image1=models.ImageField(upload_to="hotel_image/",blank=True)
    image2=models.ImageField(upload_to="hotel_image/",blank=True)
    image3=models.ImageField(upload_to="hotel_image/",blank=True)
    image4=models.ImageField(upload_to="hotel_image/",blank=True)
    image5=models.ImageField(upload_to="hotel_image/",blank=True)

    def __str__(self):
       return self.hotel_name                          