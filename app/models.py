from django.db import models
from django.contrib.auth.models import AbstractUser


class Agent(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    skype = models.URLField(null=True, blank=True)
    # avatar =

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class HouseType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class HouseStatus(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.type


class House(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True, default='Country | State')
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE, null=True, blank=True)
    price = models.FloatField()
    description = models.TextField()  # Change to CKEditor later
    # image_one =
    # image_two =
    # image_three =
    no_of_bedrooms = models.IntegerField()
    area_per_meter_square = models.IntegerField()
    no_of_bathroom = models.IntegerField()
    garage = models.BooleanField(default=False)
    status = models.ForeignKey(HouseStatus, on_delete=models.CASCADE, null=True, blank=True)
    balcony = models.BooleanField(default=False)
    deck = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    outdoor_kitchen = models.BooleanField(default=False)
    tennis_court = models.BooleanField(default=False)
    sun_room = models.BooleanField(default=False)
    cable_tv = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    concrete_flooring = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent.username

    class Meta:
        ordering = ['-created']

