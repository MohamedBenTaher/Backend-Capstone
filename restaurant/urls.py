#define URL route for index() view
from rest_framework import routers
from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'booking/tables', views.BookingViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('index/', views.index),
    path('menu/', views.MenuItemsView.as_view(),name='menu'),
    path('bookings/', views.BookingViewSet.as_view({'get':'list','post':'add','put':'edit','delete':'destroy'}),name='booking'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]