from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from app.serializers import *

class FoodCrud(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer