from django.db import models


class AdminInfo(models.Model):
    secretkey =models.CharField(max_length=200)
    debug = models.BooleanField(default=True)
    host_user = models.EmailField()
    host_password=models.CharField(max_length=200)
    account_sid= models.CharField(max_length=500)
    account_token = models.CharField(max_length=500)
    phonenumber=models.CharField(max_length=100)
