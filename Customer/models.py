from django.db import models
# Create your models here.
class CredentialInfo(models.Model):
    Account_No = models.CharField(max_length=9)
    debit_no = models.IntegerField()
    cvv_no = models.IntegerField()
    total_deposite = models.FloatField(default=0.0)
    total_loan = models.FloatField(default=0.0)
    total_balance = models.FloatField(default=0.0)
    open_time = models.DateField()
    debit_expire = models.DateField()

class LoginInfo(models.Model):
    User_ID = models.PositiveIntegerField(default=0)
    Account_No = models.CharField(max_length=9)
    login_id = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    email = models.EmailField()
    verified = models.IntegerField(default=0)
    is_login = models.IntegerField(default=0)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField()