from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import userSerializer
from .models import user


class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all().order_by('username')
    serializer_class = userSerializer