from rest_framework import serializers

from .models import user ,guser,hotel, venue,vendor

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

class venueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = venue
        fields = ('id','venue_name','desc','city','address','price','faculties','image1','image2','image3','image4','image5')

class vendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vendor
        fields = ('id','vendor_name','desc','city','address','price','food_type','image1','image2','image3','image4','image5')
