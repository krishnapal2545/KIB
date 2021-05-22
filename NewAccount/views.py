from NewAccount.models import CustomerInfo
from Customer.models import CredentialInfo , LoginInfo 
from django.shortcuts import  render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import string,random
from datetime import date


def newaccount(request):
    if request.method == 'POST':
        while True :
         account_no=''.join(random.choices(string.ascii_uppercase + string.digits,k=9))
         if CustomerInfo.objects.filter(account_no=account_no).exists() :
             continue
         else :
             break
        debit_no = ''.join(random.choices(string.digits,k=12))
        cvv_no = ''.join(random.choices(string.digits,k=3))
        total_deposite = 0.00
        total_loan = 0.00
        total_balance = 0.00
        open_time = date.today()
        name = request.POST['name']
        gender = request.POST['gender']
        nominee = request.POST['nominee']
        nominee_relat = request.POST['nominee_relat']
        phone = request.POST['phone']
        email = request.POST['email']
        addhar = request.POST['addhar']
        pan = request.POST['pan']
        profile_img = request.FILES['profile_img']
        addhar_img =  request.FILES['addhar_img']
        pan_img = request.FILES['pan_img']
        login_id = request.POST['loginid']
        password2 = request.POST['password']
        if CustomerInfo.objects.filter(aadhar=addhar).filter(pan=pan).exists():
            Result="Your Have Already Register In The KIB-Bank Check Your Account Number in Your Mail Box and Login "
            messages.error(request,Result)
            return render(request,'KIB-newaccount.html')
        user = LoginInfo.objects.create(Account_No=account_no,login_id=login_id,password=password2,email=email)
        user.save();
        subject = 'welcome to KIB'
        message = f'''Hello {name}, thank you for registering in Krishna International Bank.
        Your Account Number is {account_no}. You can Login Now in KIB Bank.'''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        user = CredentialInfo.objects.create(Account_No=account_no,debit_no=debit_no,cvv_no=cvv_no,total_deposite=total_deposite,total_loan=total_loan,total_balance=total_balance,open_time=open_time)
        user.save();
        user = CustomerInfo.objects.create(account_no=account_no,name=name,gender=gender,nominee= nominee,nominee_realt=nominee_relat,phone=phone,aadhar=addhar,pan=pan,profile_img=profile_img,aadhar_img=addhar_img,pan_img=pan_img)
        user.save();
        Result=f"Your Account Number is {account_no} don't forget your account number and do not refresh the page otherwise you lost your Account Number"
        messages.success(request,Result)
        return render(request,'KIB-newaccount.html')
    else: 
         return render(request,'KIB-newaccount.html')
