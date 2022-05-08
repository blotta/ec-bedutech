from datetime import datetime, timedelta
from django import forms
from django.forms import ModelForm
from .models import Customer, PickupLocation, ProductReturn


class ProductReturnCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductReturnCreateForm, self).__init__(*args, **kwargs)
        min_pickup_date = datetime.now() + timedelta(days=4)
        self.fields['min_pickup_date'].widget.attrs['min'] = min_pickup_date.strftime('%Y-%m-%d')
        print("hi")

    class Meta:
        model = ProductReturn
        fields = ('product', 'customer', 'customer_person', 'technician', 'reason', 'pickup_location', 'min_pickup_date')
        labels = {
            'product': 'Produto',
            'customer': 'Cliente',
            'customer_person': 'Responsável',
            'technician': 'Técnico',
            'reason': 'Motivo',
            'pickup_location': 'Ponto de Coleta',
            'min_pickup_date': 'Data mínima de coleta'

        }
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'customer_person': forms.TextInput(attrs={'class': 'form-control'}),
            'technician': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
            'pickup_location': forms.Select(attrs={'class': 'form-control'}),
            'min_pickup_date': forms.DateInput(format=('%d/%m/%Y'), attrs={
                'class': 'form-control dateinputpicker', 'placeholder': 'aaaa-mm-dd', 'min': '2022-05-10'}),
        }


class ProductReturnEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductReturnEditForm, self).__init__(*args, **kwargs)
        min_pickup_date = datetime.now() + timedelta(days=4)
        self.fields['min_pickup_date'].widget.attrs['min'] = min_pickup_date.strftime('%Y-%m-%d')
    
    class Meta:
        model = ProductReturn
        fields = ('product', 'customer', 'customer_person', 'technician',
            'reason', 'pickup_location', 'min_pickup_date', 'pickup_date', 'return_date')
        labels = {
            'product': 'Produto',
            'customer': 'Cliente',
            'customer_person': 'Responsável',
            'technician': 'Técnico',
            'reason': 'Motivo',
            'pickup_location': 'Ponto de Coleta',
            'min_pickup_date': 'Data mínima de coleta',
            'pickup_date': 'Data da coleta',
            'return_date': 'Data da finalização'
        }

        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'customer_person': forms.TextInput(attrs={'class': 'form-control'}),
            'technician': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
            'pickup_location': forms.Select(attrs={'class': 'form-control'}),

            'min_pickup_date': forms.DateInput(attrs={
                'class': 'form-control dateinputpicker', 'placeholder': 'aaaa-mm-dd', 'min': '2022-05-10'}),

            'pickup_date': forms.DateInput(attrs={
                'class': 'form-control dateinputpicker', 'placeholder': 'aaaa-mm-dd', 'min': '2022-05-10'}),

            'return_date': forms.DateInput(attrs={
                'class': 'form-control dateinputpicker', 'placeholder': 'aaaa-mm-dd', 'min': '2022-05-10'}),
        }

class PickupLocationCreateForm(forms.ModelForm):
    address_text = forms.CharField(max_length=1024, label='Pesquisar endereço',
        widget=forms.TextInput(attrs={'id': 'address-search','class': 'form-control'}))
    
    complement = forms.CharField(max_length=256, required=False, label='Complemento',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    street = forms.CharField(max_length=1024, required=True, widget=forms.HiddenInput())
    number = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput())
    cep = forms.CharField(max_length=10, required=True, widget=forms.HiddenInput())
    neighborhood = forms.CharField(max_length=256, required=True, widget=forms.HiddenInput())
    city = forms.CharField(max_length=128, required=True, widget=forms.HiddenInput())
    state = forms.CharField(max_length=2, required=True, widget=forms.HiddenInput())
    country = forms.CharField(max_length=128, required=True, widget=forms.HiddenInput())

    class Meta:
        model = PickupLocation
        fields = ('name',)
        labels = {
            'name': 'Nome'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }



class CustomerCreateForm(forms.ModelForm):
    address_text = forms.CharField(max_length=1024, label='Pesquisar endereço',
        widget=forms.TextInput(attrs={'id': 'address-search','class': 'form-control'}))
    
    complement = forms.CharField(max_length=256, required=False, label='Complemento',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    street = forms.CharField(max_length=1024, required=True, widget=forms.HiddenInput())
    number = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput())
    cep = forms.CharField(max_length=10, required=True, widget=forms.HiddenInput())
    neighborhood = forms.CharField(max_length=256, required=True, widget=forms.HiddenInput())
    city = forms.CharField(max_length=128, required=True, widget=forms.HiddenInput())
    state = forms.CharField(max_length=2, required=True, widget=forms.HiddenInput())
    country = forms.CharField(max_length=128, required=True, widget=forms.HiddenInput())

    class Meta:
        model = Customer
        fields = ('name',)
        labels = {
            'name': 'Nome'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }