from django.db import models

# Create your models here.


class Account(models.Model):
    email = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")
    creation_date = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    birth_date = models.DateField(blank=True, null=True)
    id_num = models.CharField(max_length=200, default="")
    insur_num = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    tel_num = models.CharField(max_length=200, default="")
    acc_id = models.CharField(max_length=200, null=True)
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return self.email
