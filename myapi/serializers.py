from rest_framework import serializers

from .models import user

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('name', 'data')