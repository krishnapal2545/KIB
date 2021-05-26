from django.db import models



class CredentialInfo(models.Model):
    Account_No = models.CharField(max_length=9)
    debit_no = models.IntegerField()
    cvv_no = models.IntegerField()
    total_deposite = models.FloatField(default=0.0)
    total_loan = models.FloatField(default=0.0)
    total_balance = models.FloatField(default=0.0)
    open_time = models.DateField()
    debit_expire = models.DateField()
