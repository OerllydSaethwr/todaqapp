from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup', views.signup, name='signup'),
    path('newPatient', views.patient, name='patient'),
    path('newDoctor', views.doctor, name='doctor'),
    path('doctorpage', views.doctorpage, name='doctpage'),
    path('patientpage', views.patientpage, name='patientpage'),
    path('index', views.index, name='index')
]