from django.contrib.auth.models import User
from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from NewAccount.models import CustomerInfo 


def login(request):
    if request.method == 'POST':
        account_no = request.POST['account_no']
        login_id = request.POST['login_id']
        password = request.POST['password']
        if CustomerInfo.objects.filter(account_no=account_no).exists():
            if CustomerInfo.objects.filter(login_id=login_id,password=password).exists():
              user = CustomerInfo.objects.get(account_no=account_no)
              return profile(request,1,user)
            else:
                Result={'Result':'Invalide User Name or Password'}
                return render(request,'KIB-loginpage.html',Result)
        else:
            Result={'Result':'Invalide Account Number'}
            return render(request,'KIB-loginpage.html',Result)
    else:
      return render(request,'KIB-loginpage.html')

def profile(request,c=0,user=0):
    if c==1:
     return render(request,'KIB-profile.html',{'User':user})
    else:
     return HttpResponse(" <h2> Error ! go and login first </h2>")
