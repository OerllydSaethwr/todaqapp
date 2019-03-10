from django import forms
from django.forms import TextInput
from .models import Account


class RegisterUser(forms.ModelForm):

    class Meta:
        model = Account
        exclude = ('acc_id',)

