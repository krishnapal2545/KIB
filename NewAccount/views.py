from django.core.checks import messages
from NewAccount.models import CustomerInfo
from django.shortcuts import redirect, render
import string,random

def newaccount(request):
    if request.method == 'POST':
        while True :
         account_no=''.join(random.choices(string.ascii_uppercase + string.digits,k=9))
         if CustomerInfo.objects.filter(account_no=account_no).exists() :
             continue
         else :
             break
        k = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase + string.digits,k=7))
        name = request.POST['name']
        mname = request.POST['mname']
        gender = request.POST['gender']
        bdate = request.POST['bdate']
        nominee = request.POST['nominee']
        nominee_relat = request.POST['nominee_relat']
        phone = request.POST['phone']
        email = request.POST['email']
        addhar = request.POST['addhar']
        pan = request.POST['pan']
        profile_img = 'profile_img/'+ request.POST['profile_img']
        addhar_img = 'aadhar_img/'+ request.POST['addhar_img']
        pan_img = 'pan_img/'+ request.POST['pan_img']
        login_id = request.POST['login_id']
        password = request.POST['password']

        user = CustomerInfo.objects.create(account_no=account_no,name=name,gender=gender,nominee= nominee,nominee_realt=nominee_relat,phone=phone,email=email,aadhar=addhar,pan=pan,profile_img=profile_img,aadhar_img=addhar_img,pan_img=pan_img,login_id=login_id,password=password)
        user.save();
        Result={'Result':f"Your Account Number is {account_no} don't forget your \n account number and you can login in our bank now"}
        return render(request,'KIB-newaccount.html',Result)
    else: 
         return render(request,'KIB-newaccount.html')
