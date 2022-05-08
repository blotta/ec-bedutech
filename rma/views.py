from datetime import datetime, timedelta
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Address, Customer, PickupLocation, ProductReturn

from .forms import CustomerCreateForm, PickupLocationCreateForm, ProductReturnCreateForm, ProductReturnEditForm

def listing(request):
    rma_list = ProductReturn.objects.all()
    return render(request, 'rma/listing.html', {'items': rma_list})

def details(request, rma_code):
    rma = ProductReturn.objects.get(rma_code=rma_code)
    now = datetime.now()
    return render(request, 'rma/details.html', {'item': rma, 'now': now})

def create(request):
    if request.method == 'POST':
        form = ProductReturnCreateForm(request.POST)
        if form.is_valid():
            rma = form.save()
            return redirect('details', rma.rma_code)
        else:
            return render(request, 'rma/create.html', { 'form': form })

    form = ProductReturnCreateForm
    return render(request, 'rma/create.html', { 'form': form })

def edit(request, rma_code):
    rma = ProductReturn.objects.get(rma_code=rma_code)
    form = ProductReturnEditForm(request.POST or None, instance=rma)
    if form.is_valid():
        saved = form.save()
        return redirect('details', saved.rma_code)

    return render(request, 'rma/edit.html', { 'form': form })


def pickuplocation_list(request):
    items = PickupLocation.objects.all()
    return render(request, 'pickuplocation/listing.html', {'items': items})
    
def pickuplocation_create(request):
    form = None
    if request.method == 'POST':
        form = PickupLocationCreateForm(request.POST)
        if form.is_valid():
            address = Address()
            address.street = form.cleaned_data['street']
            address.number = form.cleaned_data['number']
            address.complement = form.cleaned_data['complement']
            address.cep = form.cleaned_data['cep']
            address.neighborhood = form.cleaned_data['neighborhood']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.country = form.cleaned_data['country']
            address.save()
            pl = PickupLocation()
            pl.name = form.cleaned_data['name']
            pl.address = address
            pl.save()
            return redirect('pickuplocation_list')
        
    if form == None:
        form = PickupLocationCreateForm
    return render(request, 'pickuplocation/create.html', {'form': form, 'gapikey': settings.GOOGLE_API_KEY})


def customer_list(request):
    items = Customer.objects.all()
    return render(request, 'customer/listing.html', {'items': items})
    
def customer_create(request):
    form = None
    if request.method == 'POST':
        form = CustomerCreateForm(request.POST)
        if form.is_valid():
            address = Address()
            address.street = form.cleaned_data['street']
            address.number = form.cleaned_data['number']
            address.complement = form.cleaned_data['complement']
            address.cep = form.cleaned_data['cep']
            address.neighborhood = form.cleaned_data['neighborhood']
            address.city = form.cleaned_data['city']
            address.state = form.cleaned_data['state']
            address.country = form.cleaned_data['country']
            address.save()
            pl = Customer()
            pl.name = form.cleaned_data['name']
            pl.address = address
            pl.save()
            return redirect('customer_list')
        
    if form == None:
        form = CustomerCreateForm
    return render(request, 'customer/create.html', {'form': form, 'gapikey': settings.GOOGLE_API_KEY})