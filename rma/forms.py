from datetime import datetime, timedelta
from django import forms
from django.forms import ModelForm
from .models import ProductReturn


class ProductReturnCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductReturnCreateForm, self).__init__(*args, **kwargs)
        min_pickup_date = datetime.now() + timedelta(days=4)
        self.fields['min_pickup_date'].widget.attrs['min'] = min_pickup_date.strftime('%Y-%m-%d')
        print("hi")

    class Meta:
        model = ProductReturn
        fields = ('product', 'customer', 'customer_person', 'technician', 'reason', 'address', 'min_pickup_date')
        labels = {
            'product': 'Produto',
            'customer': 'Cliente',
            'customer_person': 'Responsável',
            'technician': 'Técnico',
            'reason': 'Motivo',
            'address': 'Endereço',
            'min_pickup_date': 'Data mínima de coleta'

        }
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'customer_person': forms.TextInput(attrs={'class': 'form-control'}),
            'technician': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Select(attrs={'class': 'form-control'}),
            'min_pickup_date': forms.DateInput(format=('%d/%m/%Y'), attrs={
                'class': 'form-control', 'type': 'date', 'placeholder': 'dd/mm/aaaa', 'min': '2022-05-10'})
        }


class ProductReturnEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductReturnEditForm, self).__init__(*args, **kwargs)
        min_pickup_date = datetime.now() + timedelta(days=4)
        self.fields['min_pickup_date'].widget.attrs['min'] = min_pickup_date.strftime('%Y-%m-%d')
        print("hi")
    
    # min_pickup_date = forms.DateField(
    #     widget=forms.DateInput(attrs={ 'class': 'form-control dateinputpicker', 'placeholder': 'aaaa-mm-dd', 'min': '2022-05-10'}),
    #     input_formats=('%d/%m/%Y',))

    class Meta:
        model = ProductReturn
        fields = ('product', 'customer', 'customer_person', 'technician',
            'reason', 'address', 'min_pickup_date', 'pickup_date', 'return_date')
        labels = {
            'product': 'Produto',
            'customer': 'Cliente',
            'customer_person': 'Responsável',
            'technician': 'Técnico',
            'reason': 'Motivo',
            'address': 'Endereço',
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
            'address': forms.Select(attrs={'class': 'form-control'}),

            'min_pickup_date': forms.DateInput(attrs={
                'class': 'form-control dateinputpicker', 'placeholder': 'aaaa-mm-dd', 'min': '2022-05-10'}),

            'pickup_date': forms.DateInput(format=('%d/%m/%Y'), attrs={
                'class': 'form-control dateinputpicker', 'placeholder': 'dd/mm/aaaa', 'min': '2022-05-10'}),

            'return_date': forms.DateInput(format=('%d/%m/%Y'), attrs={
                'class': 'form-control dateinputpicker', 'placeholder': 'dd/mm/aaaa', 'min': '2022-05-10'}),
        }