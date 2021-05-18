from django.db import models

class CustomerInfo (models.Model):
    account_no = models.CharField(max_length=9)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    nominee= models.CharField(max_length=255)
    nominee_realt = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    aadhar = models.IntegerField()
    pan = models.CharField(max_length=10)
    profile_img = models.ImageField(upload_to='profile_img/')
    aadhar_img = models.ImageField(upload_to='aadhar_img/')
    pan_img = models.ImageField(upload_to='pan_img/')
    login_id = models.EmailField()
    password = models.CharField(max_length=8)

