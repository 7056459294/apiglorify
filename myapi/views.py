from django.shortcuts import render

# Create your views here.
from rest_framework import  viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import userSerializer
from .serializers import guserSerializer
from .serializers import hotelSerializer

from .models import hotel, user,guser
#from mysite.myapi import serializers


#_______________________________________________________________________________#
#for auth api user 

#from rest_framework.authentication import SessionAuthentication
#from rest_framework.permissions import IsAuthenticatedOrReadOnly
#_______________________________________________________________________________#
#import pushbullet
#import random
#________________________________________________________________________________#
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
#__________________________________________________________________________#      
class guserViewSet(viewsets.ModelViewSet):


    queryset = guser.objects.all().order_by('full_name')
    serializer_class = guserSerializer
    #for auth api user 
    #authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticatedOrReadOnly]

    def retrieve(self, request, pk=None):
       phone_no=pk
       #usr=user.objects.get(username=username)
       if guser.objects.filter(phone_no=phone_no).exists():
           usr=guser.objects.filter(phone_no=phone_no)
           serializer=guserSerializer(usr,many=True)
           return Response(serializer.data)
       else:
          return Response(status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request,pk):
       phone_no=pk
       usr=guser.objects.get(phone_no=phone_no)
       usr.delete()
    def list(self ,request):
        usr=guser.objects.all()
        serializer=guserSerializer(usr,many=True)
        return Response(serializer.data)
    def create(sefl ,request):
        serializer=guserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def update(sefl ,request,pk):
        phone=pk
        usr=guser.objects.get(phone_no=phone)
        serializer=guserSerializer(usr,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({'msg':'data update'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def partial_update(sefl ,request,pk):
        phone=pk
        usr=guser.objects.get(phone_no=phone)
        serializer=guserSerializer(usr,data=request.data,partial=True)
        if serializer.is_valid():
           serializer.save()
           return Response({'msg':'data partial update'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#______________________________________________________________________________#

class hotelViewSet(viewsets.ModelViewSet):


    queryset = hotel.objects.all().order_by('hotel_name')
    serializer_class = hotelSerializer
    #for auth api user 
    #authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticatedOrReadOnly]

    def retrieve(self, request, pk):
       city=pk
       #usr=user.objects.get(username=username)
       if hotel.objects.filter(city=city).exists():
           hoteldata=hotel.objects.filter(city=city)
           serializer=hotelSerializer(hoteldata,many=True)
           return Response(serializer.data)
       else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request,pk):
       hotel_name=pk
       hotelname=hotel.objects.get(hotel_name=hotel_name)
       hotelname.delete()
    def list(self ,request):
        usr=hotel.objects.all()
        serializer=hotelSerializer(usr,many=True)
        return Response(serializer.data)
    def create(sefl ,request):
        serializer=hotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def update(sefl ,request,pk):
        hotel_name=pk
        hotelupdate=hotel.objects.get(hotel_name=hotel_name)
        serializer=hotelSerializer(hotelupdate,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({'msg':'data update'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def partial_update(sefl ,request,pk):
        hotel_name=pk
        usr=hotel.objects.get(hotel_name=hotel_name)
        serializer=hotelSerializer(usr,data=request.data,partial=True)
        if serializer.is_valid():
           serializer.save()
           return Response({'msg':'data partial update'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
    
#_____________________________________________________________________________________________#    
    
    
    
    
    
'''
   no=user.objects.all()
   otp_send=random.randint(1000,9999)
   pb=pushbullet.Pushbullet("o.rjt2J1T8WXwbBxnJjowPZiJhugMViAJ2")
   device=pb.devices[0]
   pb.push_sms(device,f"{no}",f"Your OTP Is:-{otp_send}")
'''













