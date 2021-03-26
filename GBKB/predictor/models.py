from django.db import models
from django.contrib.auth.models import User # default user model import
# Create your models here.
from django.utils import timezone



class review(models.Model):  # extra fields for user
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.IntegerField(null=False , blank= False, choices=(
        (None, 'select'),
        (1, 'Mirpur'),
        (2, 'Uttora'),
        (3, 'Bonani'),
        (4, 'Dhanmondi'),
        (5, 'Boshundhora'),
        (6, 'Gulshan 1'),
        (7, 'Gulshan 2'),
        ))

    sqft = models.IntegerField(default=1, null=False, blank=False)
    washRoom = models.IntegerField(default=1, null=False, blank=False)
    bedRoom = models.IntegerField(default=1, null=False, blank=False)

    roadSize = models.IntegerField(default=1, null=False, blank=False)
    lift = models.IntegerField(default=1, null=False, blank=False, choices=(
        (None, 'select'),
        (0, 'No Lift'),
        (1, 'Lift service available'),
    ))
    floor = models.IntegerField(default=1, null=False, blank=False)

    price = models.IntegerField(default=1, null=False, blank=False)




class dataSet(models.Model):  # extra fields for user

    location = models.IntegerField(null=False, blank=False, choices=(
        (None, 'select'),
        (1, 'Uttora'),
        (2, 'Dhanmondi'),
        (3, 'Boshundhora'),
        (4, 'Gulshan 1'),
        (5, 'Gulshan 2'),
    ))

    sqft = models.IntegerField(default=1, null=False, blank=False)
    washRoom = models.IntegerField(default=1, null=False, blank=False)
    bedRoom = models.IntegerField(default=1, null=False, blank=False)

    roadSize = models.IntegerField(default=1, null=False, blank=False)
    lift = models.IntegerField(default=1, null=False, blank=False, choices=(
        (None, 'select'),
        (0, 'No Lift'),
        (1, 'Lift service available'),
    ))
    floor = models.IntegerField(default=1, null=False, blank=False)

    price = models.IntegerField(default=1, null=False, blank=False)
