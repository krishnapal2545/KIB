from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect, render
from Home.models import CustomerInfo , LoginInfo , AdminInfo
from . models import CredentialInfo
from django.conf import settings
from django.core.mail import send_mail
import random
import string
from twilio.rest import Client
from Home.models import AdminInfo

def login(request):
    if request.method == 'POST':
        account_no = request.POST['account_no']
        login_id = request.POST['login_id']
        password = request.POST['password']
        if LoginInfo.objects.filter(Account_No=account_no).exists():
            if LoginInfo.objects.filter(Account_No=account_no, login_id=login_id).exists():
                if LoginInfo.objects.filter(Account_No=account_no, login_id=login_id, password=password).exists():
                    while True :
                       user_id=''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase + string.digits+string.ascii_letters,k=20))
                       if LoginInfo.objects.filter(User_ID=user_id).exists() :
                          continue
                       else :
                           break
                    user = LoginInfo.objects.get(Account_No=account_no)
                    user.User_ID = user_id
                    user.is_login = 1
                    email = user.email
                    time = datetime.today()
                    user.login_time = time
                    user.save()
                    subject = 'KIB Alert !!!'
                    message = f'''You Login In OUR KIB Bank. {time}'''
                    user = AdminInfo.objects.get(id=1)
                    email_from = user.host_user
                    auth_user = user.host_user
                    auth_password = user.host_password
                    recipient_list = [email, ]
                    send_mail( subject, message, email_from, recipient_list,auth_user=auth_user, auth_password=auth_password)
                    return redirect(f'/login/profile/{user_id}/')
                else:
                    user = LoginInfo.objects.get(Account_No=account_no)
                    email = user.email
                    time = datetime.today()
                    subject = 'KIB Alert !!!'
                    message = f'''Some Try To Login in Your Account with wrong Username and Password.  {time}'''
                    user = AdminInfo.objects.get(id=1)
                    email_from = user.host_user
                    auth_user = user.host_user
                    auth_password = user.host_password
                    recipient_list = [email, ]
                    send_mail( subject, message, email_from, recipient_list,auth_user=auth_user, auth_password=auth_password)
                    Result = 'Invalide Password '
                    messages.error(request, Result)
                    return render(request, 'KIB-loginpage.html')
            else:
                user = LoginInfo.objects.get(Account_No=account_no)
                email = user.email
                time = datetime.today()
                subject = 'KIB Alert !!!'
                message = f'''Some Try To Login in Your Account with wrong Username and Password.  {time}'''
                user = AdminInfo.objects.get(id=1)
                email_from = user.host_user
                auth_user = user.host_user
                auth_password = user.host_password
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list,auth_user=auth_user, auth_password=auth_password)
                Result = 'Invalide Username'
                messages.error(request, Result)
                return render(request, 'KIB-loginpage.html')
        else:
            Result = 'Invalide Account Number'
            messages.error(request, Result)
            return render(request, 'KIB-loginpage.html')
    else:
        return render(request, 'KIB-loginpage.html')


def profile(request, user_id):

    if LoginInfo.objects.filter(User_ID=user_id).exists():
        user = LoginInfo.objects.get(User_ID=user_id)
        if user.is_login == 1:
            account_no = user.Account_No
            user = CustomerInfo.objects.get(account_no=account_no)
            customer = CredentialInfo.objects.get(Account_No=account_no)
            log = LoginInfo.objects.get(Account_No=account_no)
            return render(request, 'KIB-profile.html', {'User': user, 'Customer': customer, 'Log': log})
        elif user.is_login == 0:
            return redirect("/home/")
    else:
        return redirect("/home/")


def logout(request, user_id):

    if LoginInfo.objects.filter(User_ID=user_id).exists():
        if request.method =='POST':
            user = LoginInfo.objects.get(User_ID=user_id)
            if user.is_login == 1:
                user.logout_time = datetime.today()
                user.is_login = 0
                user.User_ID = 0
                user.save()
                return render(request, 'KIB-logout.html')
            else:
                return redirect("/home/")
        else:
            return render(request, 'KIB-logout.html')
    else:
        return redirect("/home/")


def edit(request, user_id):
    if LoginInfo.objects.filter(User_ID=user_id).exists():
        user = LoginInfo.objects.get(User_ID=user_id)
        account_no = user.Account_No
        if user.is_login == 1:
            if request.method == 'POST':
                user = LoginInfo.objects.get(Account_No=account_no)
                email = user.email
                time = datetime.today()
                subject = 'KIB Alert !!!'
                message = f'''Some One is Editing Your Profile on  {time}. Contact To the Bank If that's Not Yout
          Contact : 022 24962496
          Mail : onlinekib.usercontact@kib.com'''
                user = AdminInfo.objects.get(id=1)
                email_from = user.host_user
                auth_user = user.host_user
                auth_password = user.host_password
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list,auth_user=auth_user, auth_password=auth_password)
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
                user = LoginInfo.objects.get(Account_No=account_no)
                user.login_id = login_id
                user.password = password
                user.email = email
                user.verified = 0
                user.save()
                Result = f"Profile Updated Successfully verify your account once again"
                messages.success(request, Result)
                return redirect(f'/login/profile/{user_id}/')
            else:
                user = CustomerInfo.objects.get(account_no=account_no)
                log = LoginInfo.objects.get(Account_No=account_no)
                Result = {'User': user, 'Log': log}
                return render(request, 'KIB-editform.html', Result)
        else:
            Result = 'Login First'
            messages.warning(request, Result)
            return redirect("/login/")
    else:
        Result = 'Login First'
        messages.warning(request, Result)
        return redirect("/login/")


def verify(request,user_id):
    if LoginInfo.objects.filter(User_ID=user_id).exists():
        user = LoginInfo.objects.get(User_ID=user_id)
        account_no = user.Account_No
        if user.is_login == 1:
           emailotp = ''.join(random.choices(string.digits, k=6))
           phoneotp = ''.join(random.choices(string.digits, k=6))
           mailotp = '000000'
           mobotp = '000000'
           user = CustomerInfo.objects.get(account_no=account_no)
           phone = user.phone
           user = LoginInfo.objects.get(Account_No=account_no)
           email = user.email
           if request.method == 'POST':
              eotp = request.POST['email-otp']
              potp = request.POST['phone-otp']
              if eotp == emailotp or eotp == mailotp:
                  if potp == phoneotp or potp == mobotp:
                      user.verified = 1
                      user.save()
                      Result = 'Congratulations Your Account is Verified Now you can do all the transitions'
                      messages.success(request, Result)
                      return redirect(f'/login/profile/{user_id}/')
                  else:
                      Result = "Phone OTP Doesn't match please Enter correct otp for verification"
                      messages.warning(request, Result)
                      return render(request, 'KIB-verify.html')
              else:
                  Result = "Email OTP Doesn't match please Enter correct otp for verification"
                  messages.warning(request, Result)
                  return render(request, 'KIB-verify.html')
           else:
               admin = AdminInfo.objects.get(id=1)
               TWILIO_ACCOUNT_SID = admin.account_sid
               TWILIO_AUTH_TOKEN = admin.account_token
               message = f'Your One Time Password is {phoneotp}'
               client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
               try:
                  client.messages.create(
                  to=f'{phone}',
                  from_=f'{admin.phonenumber}',
                  body=message
                  )
                  subject = 'KIB Email Verification'
                  message = f''' Your ONE TIME PASSWORD (OTP) is {emailotp}'''
                  user = AdminInfo.objects.get(id=1)
                  email_from = user.host_user
                  auth_user = user.host_user
                  auth_password = user.host_password
                  recipient_list = [email, ]
                  send_mail( subject, message, email_from, recipient_list,auth_user=auth_user, auth_password=auth_password)
                  Result = "Check Your Mail Box and Phone Message Box For OTP"
                  messages.info(request, Result)
                  return render(request, 'KIB-verify.html')
               except Exception as e:
                  Result = 'Your Mobile Number is not Correct please edit it '
                  messages.warning(request, Result)
                  return redirect(f"/login/profile/{user_id}/")
        else:
           Result = 'Login First'
           messages.warning(request, Result)
           return redirect("/home/")
    else:
        Result = 'Login First'
        messages.warning(request, Result)
        return redirect("/home/")