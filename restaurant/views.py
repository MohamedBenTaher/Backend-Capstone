from django.shortcuts import render
from .serializers import UserSerializer,MenuSerializer,BookingSerializer
from django.contrib.auth.models import User
from .models import Menu,Booking
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    # def get_queryset(self):
    #     return User.objects.all().filter(user=self.request.user)

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # def get_queryset(self):
    #     return User.objects.all().filter(user=self.request.user)