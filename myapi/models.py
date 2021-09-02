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