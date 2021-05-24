from django.db import models
# Create your models here.
class CredentialInfo(models.Model):
    Account_No = models.CharField(max_length=9)
    debit_no = models.IntegerField()
    cvv_no = models.IntegerField()
    total_deposite = models.FloatField()
    total_loan = models.FloatField()
    total_balance = models.FloatField()
    open_time = models.DateField()
    debit_expire = models.DateField()

class LoginInfo(models.Model):
    Account_No = models.CharField(max_length=9)
    login_id = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    email = models.EmailField()
    verified = models.IntegerField(default=0)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField()