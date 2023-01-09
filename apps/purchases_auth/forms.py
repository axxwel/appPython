from django import forms

from purchases_auth.models import Order

class Order_form(forms.ModelForm):
    class Meta:
        model = Order
        
        fields = [
            'branch',
            'process',
            'purchase_type',
            'payment_method',
            'product',
            'price',
        ]

class Order_form_auth(forms.ModelForm):
    class Meta:
        model = Order
        
        fields = [
            'controler_comment',
            'controler_auth',
        ]
    