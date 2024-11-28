from django_filters import FilterSet
from .models import *


class HotelFilterSet(FilterSet):
    class Meta:
        model = Hotel
        fields = {
             'country': ['exact'],
            'city': ['exact'],
            'start': ['exact'],

        }


class RoomFilterSet(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_types': ['exact'],
            'room_status': ['exact'],
            'all_inclusive': ['exact'],
            'room_price': ['gt', 'lt'],

        }