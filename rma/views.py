from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import ProductReturn

from .forms import ProductReturnCreateForm, ProductReturnEditForm

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
    # rma = get_object_or_404(ProductReturn, rma_code=rma_code)
    rma = ProductReturn.objects.get(rma_code=rma_code)
    form = ProductReturnEditForm(request.POST or None, instance=rma)
    if form.is_valid():
        saved = form.save()
        return redirect('details', saved.rma_code)

    return render(request, 'rma/edit.html', { 'form': form })
