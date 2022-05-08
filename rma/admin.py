from django.contrib import admin

from .models import Address, Customer, PickupLocation, ProductReturn

admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(ProductReturn)

admin.site.register(PickupLocation)