from datetime import date, datetime
import email
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from NewAccount.models import CustomerInfo
from . models import CredentialInfo, LoginInfo
from django.conf import settings
from django.core.mail import send_mail

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
    account_no = 0
    return redirect("/login/")
