from django import forms
from .models import Account


class AccountCreateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'username', 'first_name', 
                'last_name', 'city', 'house_number', 
                'apartment_number', 'zip_code']