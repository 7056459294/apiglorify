from rest_framework import serializers

from .models import user ,guser

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('id','username', 'phone_no','email','password')

class guserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = guser
        fields = ('id','full_name','email','phone_no','password')