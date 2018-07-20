from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    pass


class House(models.Model):
    street = models.CharField(max_length=255)
    st_number = models.CharField(max_length=255)
    apartment_amount = models.CharField(max_length=255)
    build_date = models.DateField()


class Housemates(models.Model):
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    apartment = models.CharField(max_length=255)
    house = models.ForeignKey('House', on_delete=models.PROTECT)
