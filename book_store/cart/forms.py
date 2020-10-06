from django import forms

class CartAddBookForm(forms.Form):
    quantity = 1
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
