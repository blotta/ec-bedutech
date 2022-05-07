from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def listing(request):
    return render(request, 'rma/listing.html', {})