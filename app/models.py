from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    pass

    class Meta:
        app_label = 'app'
        db_table = 'user'


class House(models.Model):
    street = models.CharField(max_length=255)
    st_number = models.IntegerField()
    apartment_amount = models.IntegerField()
    build_date = models.DateField()

    class Meta:
        app_label = 'app'
        db_table = 'house'

    def __str__(self):
        return 'Based on {}, {} St. / was built in {}'.format(self.st_number, self.street, self.build_date.strftime("%Y"))


class Housemate(models.Model):
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    apartment = models.IntegerField()
    house = models.ForeignKey('House', on_delete=models.PROTECT)

    class Meta:
        app_label = 'app'
        db_table = 'housemate'

    def __str__(self):
        return '{} {} {} / {}, {} St. {} Apt.'.format(self.first_name, self.middle_name, self.last_name,
                                                     self.house.st_number, self.house.street, self.apartment)
