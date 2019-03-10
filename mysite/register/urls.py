from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('patient', views.patient, name='patient'),
    path('doctor', views.doctor, name='doctor'),
    path('doctorpage', views.doctorpage, name='doctpage'),
    path('patientpage', views.patientpage, name='patientpage')
]