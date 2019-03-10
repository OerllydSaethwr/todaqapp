from django.shortcuts import render

from register.models import Account
from .forms import RegisterUser, Login
from django.shortcuts import redirect
from django.contrib.auth.models import User
import requests
import json

# Create your views here.


def landing(request):
    return render(request, 'register/newIndex.html', {})


def index(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data.get('email')
            password = data.get('password')
            try:
                acc = Account.objects.get(email=email)
                if acc.password == password:
                    return redirect('patient')
                else:
                    print("false")
                    return redirect('index')
            except:
                print("Invalid email!")
                return redirect('index')
    else:
        form = Login()
    return render(request, 'register/index.html', {'form': form})


def signup(request):
    context = {}
    return render(request, 'register/signup.html', context)


def patient(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data.get('email')
            phone = data.get('tel_num')
            lastname = data.get('last_name')
            firstname = data.get('first_name')
            city = "London"
            postalcode = "W3 6DT"
            provreg = "London"
            street = "Victoria Road"
            country = "UK"
            p1 = "{\n\t\"type\": \"account\",\n    \"data\": {\n    \t\"attributes\": {\n\t\t\t\"account-type\": \"individual\",\n\t\t\t\"admin-email\": \""
            p2 = "\",\n\t\t\t\"contact\": {\n\t\t\t   \"email\": \""
            p3 = "\",\n\t\t\t   \"phone\": \""
            p4 = "\",\n\t\t\t   \"last-name\": \""
            p5 = "\",\n\t\t\t   \"first-name\": \""
            p6 = "\",\n\t\t\t   \"address\": {\n\t\t   \t\t\t\"city\": \""
            p7 = "\",\n\t\t             \"postal-code\": \""
            p8 = "\",\n\t\t             \"province-region\": \""
            p9 = "\",\n\t\t             \"street-address-1\": \""
            p10 = "\",\n\t\t             \"country\": \""
            p11 = "\"\n\t\t\t   }\n\t   \t\t}\n\t\t}\n    }\n}"
            payload = p1 + email + p2 + email + p3 + phone + p4 + lastname + p5 + firstname + p6 + city + p7 + postalcode + p8 + provreg + p9 + street + p10 + country + p11
            url = 'https://api.todaqfinance.net/accounts'
            headers = {
                'Content-Type': 'application/json',
                'x-api-key': 'fd0ae52b-0866-449e-8e60-d0b12525cbbc'
            }
            response = requests.request('POST', url, headers=headers, data=payload, allow_redirects=False)
            d2 = response.json()
            form.save()
            acc = Account.objects.latest('id')
            acc.acc_id = d2['data'][0]['id']
            acc.save()

            user = User.objects.create_user(username=data.get('email'), email=data.get('email'), password=data.get('password'))
            user.save()

            return redirect('index')
    else:
        form = RegisterUser()
    return render(request, 'register/newPatient.html', {'form': form})


def doctor(request):
    context = {}
    return render(request, 'register/newDoctor.html', context)


def doctorpage(request):
    context = {}
    return render(request, 'register/doctorpage.html', context)


def patientpage(request):
    context = {}
    return render(request, 'register/patientpage.html', context)



