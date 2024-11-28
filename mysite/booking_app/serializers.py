from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileOwnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserProfileReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']


class HotelListSerializers(serializers.ModelSerializer):
    hotel_images = HotelImageSerializers(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = ['name_hotel', 'country', 'city', 'hotel_images', 'start']


class HotelRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name_hotel']


class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class RoomSerializers(serializers.ModelSerializer):
    room_images = RoomImageSerializers(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_types', 'room_status', 'room_price', 'room_images']


class RoomDetailSerializers(serializers.ModelSerializer):
    room_images = RoomImageSerializers(read_only=True, many=True)
    hotell_room = HotelRoomSerializers(read_only=True)
    class Meta:
        model = Room
        fields = ['room_number','room_description', 'room_types', 'room_status', 'room_price', 'room_images', 'hotell_room']


class ReviewSerializers(serializers.ModelSerializer):
    user_name = UserProfileReviewSerializers(read_only=True)
    class Meta:
        model = Review
        fields = ['user_name', 'text', 'stars', 'parent']


class BookingSerializers(serializers.ModelSerializer):
    user_book = UserProfileOwnerSerializers(read_only=True)
    class Meta:
        model = Booking
        fields = ['hotel_book', 'room_book', 'user_book', 'total_price']


class HotelDetailSerializers(serializers.ModelSerializer):
    hotel_images = HotelImageSerializers(read_only=True, many=True)
    reviews = ReviewSerializers(read_only=True, many=True)
    owner = UserProfileOwnerSerializers(read_only=True)
    rooms = RoomSerializers(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = ['name_hotel', 'country', 'address', 'city', 'hotel_images', 'start', 'reviews', 'owner', 'created_date', 'rooms']
