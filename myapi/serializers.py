from rest_framework import serializers

from .models import user ,guser,hotel

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('id','username', 'phone_no','email','password')

class guserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = guser
        fields = ('id','full_name','email','phone_no','password')

class hotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hotel
        fields = ('id','hotel_name','desc','city','address','price','faculties','image1','image2','image3','image4','image5')