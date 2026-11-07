from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

  class Meta:
    model = Order
    fields = ['full_name', 'phone', 'address', 'payment_method']
    widgets = {
        'full_name': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваше ПІБ'}
        ),
        'phone': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '+380XXXXXXXXX'}
        ),
        'address': forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Адреса доставки',
            }
        ),
        'payment_method': forms.Select(attrs={'class': 'form-control'}),
    }