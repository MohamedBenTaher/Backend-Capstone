from django.shortcuts import render
from .serializers import UserSerializer,MenuSerializer,BookingSerializer
from django.contrib.auth.models import User
from .models import Menu,Booking
from rest_framework import generics
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
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    # def get_queryset(self):
    #     return User.objects.all().filter(user=self.request.user)