from msilib.schema import Property
import uuid
from django.db import models
from django.utils import timezone

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating 'created_at' and 'updated_at' field
    """
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        abstract = True

class Address(models.Model):
    street = models.CharField(max_length=1024)
    number = models.IntegerField()
    complement = models.CharField(max_length=256, blank=True, null=True)
    cep = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.street}, {self.number} - {self.neighborhood}, {self.city} - {self.state}/{self.cep}"



class Customer(models.Model):
    name = models.CharField(max_length=1024)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class ProductReturn(TimeStampedModel):
    # rma_code = models.CharField(max_length=30, unique=True)
    rma_code = models.UUIDField(unique=True, default=uuid.uuid4)
    product = models.CharField(max_length=256)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    customer_person = models.CharField(max_length=128)
    technician = models.CharField(max_length=128)
    reason = models.TextField(blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    min_pickup_date = models.DateField() # createdat + 7
    pickup_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)

    STATUS_CREATED = 'CREATED'
    STATUS_PICKEDUP = 'PICKEDUP'
    STATUS_FINALIZED = 'FINALIZED'

    @property
    def status(self):
        if self.return_date:
            return ProductReturn.STATUS_FINALIZED
        elif self.pickup_date:
            return ProductReturn.STATUS_PICKEDUP
        else:
            return ProductReturn.STATUS_CREATED
    
    def status_str(self):
        st = self.status
        if st == ProductReturn.STATUS_CREATED:
            return f"Aguardando coleta a partir de"
        elif st == ProductReturn.STATUS_PICKEDUP:
            return f"Coletado em"
        
        return f"Finalizado em"
    
    def status_date(self):
        st = self.status
        if st == ProductReturn.STATUS_CREATED:
            return self.min_pickup_date
        elif st == ProductReturn.STATUS_PICKEDUP:
            return self.pickup_date
        
        return self.return_date