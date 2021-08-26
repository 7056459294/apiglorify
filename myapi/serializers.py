from rest_framework import serializers

from .models import user ,user2

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('id','username', 'phone_no','email','password')

class user2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user2
        fields = ("id",'username', 'phone_no','email','password')