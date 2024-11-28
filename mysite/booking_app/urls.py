from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'hotel', HotelListViewSet, basename='hotels')
router.register(r'hotel-detail', HotelDetailViewSet, basename='hotel-detail')
router.register(r'hotel_image', HotelImageViewSet, basename='hotel_image')
router.register(r'room_image', RoomImageViewSet, basename='room_image')
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'room-detail', RoomDetailViewSet, basename='room-detail')
router.register(r'room', RoomViewSet, basename='room')
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'booking', BookingViewSet, basename='booking')



urlpatterns = [
    path('', include(router.urls)),
]