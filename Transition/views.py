from django.shortcuts import redirect, render
from Home.models import CustomerInfo,LoginInfo

def transition(request,user_id=None):

    if user_id is not None:
        if LoginInfo.objects.filter(User_ID=user_id).exists:
            log = LoginInfo.objects.get(User_ID=user_id)
            user = CustomerInfo.objects.get(account_no=log.Account_No)
            return render(request,'KIB-pay.html',{'User':user,'Log':log})
        else:
            return redirect('/transition/')
    else:
        return render(request,'KIB-pay.html')