from datetime import datetime
from . sms import sms
import string
from django.contrib import messages
from django.shortcuts import redirect, render
from NewAccount.models import CustomerInfo
from . models import CredentialInfo, LoginInfo
from django.conf import settings
from django.core.mail import send_mail
import random ,string

account_no = 0


def login(request):
    if request.method == 'POST':
        global account_no
        account_no = request.POST['account_no']
        login_id = request.POST['login_id']
        password = request.POST['password']
        if LoginInfo.objects.filter(Account_No=account_no).exists():
            if LoginInfo.objects.filter(Account_No=account_no, login_id=login_id).exists():
                if LoginInfo.objects.filter(Account_No=account_no, login_id=login_id, password=password).exists():
                    user = LoginInfo.objects.get(Account_No=account_no)
                    email = user.email
                    time = datetime.today()
                    subject = 'KIB Alert !!!'
                    message = f'''You Login In OUR KIB Bank. {time}'''
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email, ]
                    send_mail(subject, message, email_from, recipient_list)
                    user = LoginInfo.objects.get(Account_No=account_no)
                    user.login_time = time
                    user.save()
                    if user.verified == 0:
                        Result = 'Your Account Is not Verified Please Verify your Email and Phone number for any transcition.'
                        messages.warning(request, Result)
                    return redirect('profile/')
                else:
                    user = LoginInfo.objects.get(Account_No=account_no)
                    email = user.email
                    time = datetime.today()
                    subject = 'KIB Alert !!!'
                    message = f'''Some Try To Login in Your Account with wrong Username and Password.  {time}'''
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email, ]
                    send_mail(subject, message, email_from, recipient_list)
                    Result = 'Invalide Password '
                    messages.error(request, Result)
                    return render(request, 'KIB-loginpage.html')
            else:
                user = LoginInfo.objects.get(Account_No=account_no)
                email = user.email
                time = datetime.today()
                subject = 'KIB Alert !!!'
                message = f'''Some Try To Login in Your Account with wrong Username and Password.  {time}'''
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail(subject, message, email_from, recipient_list)
                Result = 'Invalide Username'
                messages.error(request, Result)
                return render(request, 'KIB-loginpage.html')
        else:
            Result = 'Invalide Account Number'
            messages.error(request, Result)
            return render(request, 'KIB-loginpage.html')
    else:
        return render(request, 'KIB-loginpage.html')


def profile(request):
    if account_no:
        user = CustomerInfo.objects.get(account_no=account_no)
        customer = CredentialInfo.objects.get(Account_No=account_no)
        log = LoginInfo.objects.get(Account_No=account_no)
        return render(request, 'KIB-profile.html', {'User': user, 'Customer': customer, 'Log': log})
    else:
        Result = 'You Have To login to see your Profile'
        messages.warning(request, Result)
        return redirect("/login/")


def logout(request):
    global account_no
    user = LoginInfo.objects.get(Account_No=account_no)
    user.logout_time = datetime.today()
    user.save()
    account_no = 0
    return redirect("/login/")


def edit(request):
    global account_no
    if account_no:
        if request.method == 'POST':
            user = LoginInfo.objects.get(Account_No=account_no)
            email = user.email
            time = datetime.today()
            subject = 'KIB Alert !!!'
            message = f'''Some One is Editing Your Profile on  {time}. Contact To the Bank If that's Not Yout
        Contact : 022 24962496
        Mail : onlinekib.usercontact@kib.com'''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            name = request.POST['name']
            gender = request.POST['gender']
            nominee = request.POST['nominee']
            nominee_relat = request.POST['nominee_relat']
            phone = request.POST['phone']
            email = request.POST['email']
            aadhar = request.POST['addhar']
            pan = request.POST['pan']
            profile_img = request.FILES['profile_img']
            aadhar_img = request.FILES['aadhar_img']
            pan_img = request.FILES['pan_img']
            login_id = request.POST['loginid']
            password = request.POST['password']
            user = LoginInfo.objects.get(Account_No=account_no)
            user.login_id = login_id
            user.password = password
            user.email = email
            user.verified = 0
            user.save()
            user = CustomerInfo.objects.get(account_no=account_no)
            user.name = name
            user.gender = gender
            user.nominee = nominee
            user.nominee_realt = nominee_relat
            user.phone = phone
            user.aadhar = aadhar
            user.pan = pan
            user.profile_img = profile_img
            user.aadhar_img = aadhar_img
            user.pan_img = profile_img
            user.save()
            Result = f"Profile Updated Successfully"
            messages.success(request, Result)
            return redirect('/login/profile/')

        else:
            user = CustomerInfo.objects.get(account_no=account_no)
            log = LoginInfo.objects.get(Account_No=account_no)
            Result = {'User': user, 'Log': log}
            return render(request, 'KIB-editform.html', Result)

    else:
        Result = 'Login First'
        messages.warning(request, Result)
        return redirect("/login/")

emailotp=''.join(random.choices(string.digits,k=6))
phoneotp=''.join(random.choices(string.digits,k=6))


def verify(request):
    global account_no
    if account_no:
        user = LoginInfo.objects.get(Account_No=account_no)
        email = user.email
        user = CustomerInfo.objects.get(account_no=account_no)
        phone = user.phone
        if request.method == 'POST':
            eotp = request.POST['email-otp']
            potp = request.POST['phone-otp']
            print(f'{eotp},{potp}')
            print(emailotp)
            print(phoneotp)
            if eotp == emailotp and potp == phoneotp:
                  user.verified = 1
                  user.save();
                  Result = 'Congratulations Your Account is Verified Now you can do all the transitions'
                  messages.success(request, Result)
                  return redirect('/login/profile/')  
            else:
                Result = "OTP Doesn't match please Enter correct otp for verification"
                messages.warning(request, Result)
        else:
            sms(phoneotp,phone)
            subject = 'KIB Email Verification'
            message = f''' Your ONE TIME PASSWORD (OTP) is {emailotp}'''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            Result = "Check Your Mail Box and Phone Message Box For OTP"
            messages.info(request, Result)
        return render(request, 'KIB-verify.html')
    else:
        Result = 'Login First'
        messages.warning(request, Result)
        return redirect("/login/")
