from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('simpleUser', 'simpleUser'),
        ('ownerUser', 'ownerUser')
    )
    user_role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='simpleUser')
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    age = models.PositiveIntegerField(verbose_name=[MinValueValidator(15),
                                                    MaxValueValidator(100)], null=True, blank=True)

class Hotel(models.Model):
    name_hotel = models.CharField(max_length=30)
    hotel_description = models.TextField()
    address = models.CharField(max_length=35)
    city = models.CharField(max_length=55)
    country = models.CharField(max_length=35)
    start = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                    MaxValueValidator(5)])
    hotel_video = models.FileField(upload_to='hotel_video/', null=True, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.name_hotel}-{self.country}'


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_images')
    hotel_image = models.ImageField(upload_to='hotel_image/', null=True, blank=True)


class Room(models.Model):
    room_number = models.PositiveSmallIntegerField()
    hotell_room = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    TYPES = (
        ('люкс', 'люкс'),
        ('семейный', 'семейный'),
        ('одноместный', 'одноместный'),
        ('двухместный', 'двухместный')
    )
    room_types = models.CharField(max_length=16, choices=TYPES)
    STATUS = (
        ('свободен', 'свободен'),
        ('забронирован', 'забронирован'),
        ('занят', 'занят'),
    )
    room_status = models.CharField(max_length=16, choices=STATUS, default='свободен')
    room_price = models.PositiveIntegerField()
    all_inclusive = models.BooleanField(default=True)
    room_description = models.TextField()

    def __str__(self):
        return f'{self.hotell_room}, {self.room_types}, {self.room_number}'


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    room_image = models.ImageField(upload_to='room_image/', null=True, blank=True)


class Review(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.user_name}, {self.hotel}, {self.stars}'


class Booking(models.Model):
    hotel_book = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_book = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_book = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    chek_in = models.DateTimeField()
    chek_uot = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_BOOK_ROOM = (
        ('отменено', 'отменено'),
        ('подверждено', 'подверждено')
    )
    status_book = models.CharField(max_length=16, choices=STATUS_BOOK_ROOM)

    def __str__(self):
        return f'{self.user_book}, {self.hotel_book}, {self.room_book}, {self.status_book }'