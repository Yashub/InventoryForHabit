from django import forms
from django.forms import ModelForm
from .models import Address, DonationData

class AddressForm(ModelForm):
    class Meta:
            model = Address
            fields = ['address_line_1', 'address_line_2', 'city', 'state', 'zip', 'country']

class DonationDataForm(ModelForm):
    class Meta:
            model = DonationData
            fields = ['donation_id', 'date', 'day_of_week', 'type', 'receipt_declined', 'address', 'add_to_mailing_list', 'volunteer_interest', 'num_items', 'notes']

