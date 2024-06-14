from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import render
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer


def home(request):
    return render(request, 'index.html')

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]