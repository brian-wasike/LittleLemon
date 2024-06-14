from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Booking, Menu

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'