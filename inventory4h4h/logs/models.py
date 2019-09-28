from django.db import models
from django_countries.fields import CountryField
from django.contrib.localflavor.us.us_states import STATE_CHOICES


class DonationData(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    id = models.CharField(max_length=100)
    date = models.DateTimeField()
    day_of_week = models.DateTimeField()
    type = models.CharField(max_length=100)
    receipt_declined = models.BooleanField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE,)
    add_to_mailing_list = models.BooleanField()
    volunteer_interest = models.BooleanField()
    num_donations = models.IntegerField()
    notes = models.CharField(max_length=400)

class Address(models.Model):
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True)
    zip = models.IntegerField(max_length=10)
    country =  CountryField()

# Create your models here.
