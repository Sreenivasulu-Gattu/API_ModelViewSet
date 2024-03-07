from rest_framework import serializers
from app.models import *

class FoodModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'