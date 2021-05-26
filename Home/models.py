from django.db import models


class AdminInfo(models.Model):
    secretkey =models.CharField(max_length=200)
    debug = models.BooleanField(default=True)
    host_user = models.EmailField()
    host_password=models.CharField(max_length=200)
    account_sid= models.CharField(max_length=500)
    account_token = models.CharField(max_length=500)
    phonenumber=models.CharField(max_length=100)

class CustomerInfo(models.Model):
    account_no = models.CharField(max_length=9)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    nominee= models.CharField(max_length=255)
    nominee_realt = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    aadhar = models.IntegerField()
    pan = models.CharField(max_length=10)
    profile_img = models.ImageField(upload_to='profile_img/')
    aadhar_img = models.ImageField(upload_to='aadhar_img/')
    pan_img = models.ImageField(upload_to='pan_img/')

class LoginInfo(models.Model):
    User_ID = models.CharField(max_length=100,default=0)
    Account_No = models.CharField(max_length=9)
    login_id = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    email = models.EmailField()
    verified = models.IntegerField(default=0)
    is_login = models.IntegerField(default=0)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField()

