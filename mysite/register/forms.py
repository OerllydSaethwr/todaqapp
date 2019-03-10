from django import forms
from django.forms import TextInput
from .models import Account


class RegisterUser(forms.ModelForm):

    class Meta:
        model = Account
        exclude = ('acc_id','is_doctor')


class Login(forms.Form):

    email = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


