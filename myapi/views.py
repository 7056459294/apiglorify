from django.shortcuts import render

# Create your views here.
from rest_framework import  viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import userSerializer
from .serializers import guserSerializer
from .models import user,guser
#from mysite.myapi import serializers


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
    
    def retrieve(self, request, pk=None):
        username=pk
        #usr=user.objects.get(username=username)
        usr=user.objects.filter(username=username)
        serializer=userSerializer(usr,many=True)
        return Response(serializer.data)
    def destroy(self, request,pk):
        username=pk
        usr=user.objects.get(username=username)
        usr.delete()
        
class guserViewSet(viewsets.ModelViewSet):


    queryset = guser.objects.all().order_by('full_name')
    serializer_class = guserSerializer
    #for auth api user 
    #authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticatedOrReadOnly]

    def retrieve(self, request, pk=None):
       phone_no=pk
       #usr=user.objects.get(username=username)
       usr=guser.objects.get(phone_no=phone_no)
       serializer=guserSerializer(usr)
       return Response(serializer.data)
    def destroy(self, request,pk):
       phone_no=pk
       usr=guser.objects.get(phone_no=phone_no)
       usr.delete()
    
    
    
    
    
    
    
    
    
'''
   no=user.objects.all()
   otp_send=random.randint(1000,9999)
   pb=pushbullet.Pushbullet("o.rjt2J1T8WXwbBxnJjowPZiJhugMViAJ2")
   device=pb.devices[0]
   pb.push_sms(device,f"{no}",f"Your OTP Is:-{otp_send}")
'''