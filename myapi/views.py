from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import userSerializer
from .models import user,user2
#import pushbullet
#import random

class userViewSet(viewsets.ModelViewSet):


    queryset = user.objects.all().order_by('username')
    serializer_class = userSerializer

class user2ViewSet(viewsets.ModelViewSet):


    queryset = user2.objects.all().order_by('username')
    serializer_class = userSerializer

'''
   no=user.objects.all()
   otp_send=random.randint(1000,9999)
   pb=pushbullet.Pushbullet("o.rjt2J1T8WXwbBxnJjowPZiJhugMViAJ2")
   device=pb.devices[0]
   pb.push_sms(device,f"{no}",f"Your OTP Is:-{otp_send}")
'''