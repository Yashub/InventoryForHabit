from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import DonationDataForm

def index(request):
    donations_list = DonationDataForm.objects.all()
    context = {
        'donations_list' : donations_list,
    }
    return render(request, 'index.html', context)

def detail(request, donation_id):
    donation=get_object_or_404(DonationDataForm, pk=donation_id)
    return render(request, 'detail.html', donation)

#Create your views here.
