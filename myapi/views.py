from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import userSerializer
from .models import user,user2

#for auth api user 

#from rest_framework.authentication import SessionAuthentication
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

#import pushbullet
#import random

class userViewSet(viewsets.ModelViewSet):


    queryset = user.objects.all().order_by('username')
    serializer_class = userSerializer
    #for auth api user 
    #authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticatedOrReadOnly]

class user2ViewSet(viewsets.ModelViewSet):


    queryset = user2.objects.all().order_by('username')
    serializer_class = userSerializer
    #for auth api user 
    #authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticatedOrReadOnly]

'''
   no=user.objects.all()
   otp_send=random.randint(1000,9999)
   pb=pushbullet.Pushbullet("o.rjt2J1T8WXwbBxnJjowPZiJhugMViAJ2")
   device=pb.devices[0]
   pb.push_sms(device,f"{no}",f"Your OTP Is:-{otp_send}")
'''