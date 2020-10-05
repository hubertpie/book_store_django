from django import forms

BOOK_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]

class CartAddBookForm(forms.Form):
    quantity = 1
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
