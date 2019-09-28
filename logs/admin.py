from django.contrib import admin

from .models import DonationData, Address

admin.site.register(DonationData)
admin.site.register(Address)

# Register your models here.
