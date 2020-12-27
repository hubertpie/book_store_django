from django import forms
from .models import Account


class AccountCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Account
        fields = ['email', 'username', 'password']

    def save(self, commit=True):
        user = super(AccountCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user