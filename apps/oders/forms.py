from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    """Форма оформления заказа."""
    class Meta:
        model = Order
        fields = ['address', 'phone', 'comment', 'payment_method']
        widgets = {
        'address': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Улица, дом, квартира',
        }),
        'phone': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '+7 999 123-45-67',
        }),
        'comment': forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
        'placeholder': 'Пожелания к заказу (необязательно)',
        }),
        'payment_method': forms.RadioSelect(),
        }
        labels = {
        'address': 'Адрес доставки',
        'phone': 'Телефон',
        'comment': 'Комментарий',
        'payment_method': 'Способ оплаты',
        }
    def clean_phone(self):
        """Простая валидация телефона."""
        phone = self.cleaned_data['phone']
        digits = ''.join(c for c in phone if c.isdigit())
        if len(digits) < 10:
            raise forms.ValidationError('Введите корректный номер телефона.')
        return phone
    def clean_address(self):
        """Адрес не должен быть короче 10 символов."""
        address = self.cleaned_data['address']
        if len(address.strip()) < 10:
            raise forms.ValidationError('Адрес слишком короткий.')
        return address