from django.contrib import messages
from django.shortcuts import redirect, render
from Home.models import LoginInfo, CustomerInfo
from Customer.models import *
from . models import *
import string , random


def bazaar(request, user_id=None):
    mobile = Mobiles.objects.all()
    electro = Electronics.objects.all()
    fashion = Fashion.objects.all()
    home = Home.objects.all()
    beauty = Beauty.objects.all()
    furniture = Furniture.objects.all()
    medicine = Medicine.objects.all()
    if user_id is not None:
        if LoginInfo.objects.filter(User_ID=user_id).exists:
            log = LoginInfo.objects.get(User_ID=user_id)
            user = CustomerInfo.objects.get(account_no=log.Account_No)
            if request.method == 'POST':
                account_no = log.Account_No
                title = request.POST['title']
                price = request.POST['price']
                descrip = request.POST['descrip']
                image_url = request.POST['image_url']
                if ShoppingCart.objects.filter(account_no=account_no,title=title,price=price,descrip=descrip).exists():
                    Result = 'Your Product is added in your Cart'
                    messages.success(request,Result)
                else:
                    user = ShoppingCart.objects.create(
                    account_no=account_no, title=title, price=price, descrip=descrip, image_url=image_url)
                    user.save()
                Products = {'Mobiles': mobile, 'Electros': electro, 'Fashions': fashion, 'Homes': home,
                            'Beauty': beauty, 'Furnitures': furniture, 'Medicines': medicine, 'Log': log, 'User': user}
            else:
                Products = {'Mobiles': mobile, 'Electros': electro, 'Fashions': fashion, 'Homes': home,
                            'Beauty': beauty, 'Furnitures': furniture, 'Medicines': medicine, 'Log': log, 'User': user}
        else:
            Products = {'Mobiles': mobile, 'Electros': electro, 'Fashions': fashion,
                        'Homes': home, 'Beauty': beauty, 'Furnitures': furniture, 'Medicines': medicine}
    else:
        Products = {'Mobiles': mobile, 'Electros': electro, 'Fashions': fashion,
                    'Homes': home, 'Beauty': beauty, 'Furnitures': furniture, 'Medicines': medicine}
    return render(request, 'KIB-bazaar.html', Products)


def cart(request, user_id):
    if LoginInfo.objects.filter(User_ID=user_id).exists:
        log = LoginInfo.objects.get(User_ID=user_id)
        user = CustomerInfo.objects.get(account_no=log.Account_No)
        cred = CredentialInfo.objects.get(Account_No=log.Account_No)
        cart = ShoppingCart.objects.filter(account_no=log.Account_No)
        total = 0
        for i in cart:
            total = total + i.price
        if request.method == 'POST':
            if total <= cred.total_deposite:
             total = request.POST['total']
             account_no = log.Account_No
             while True:
                order_id=''.join(random.choices(string.ascii_uppercase + string.digits,k=20))
                if OrderList.objects.filter(order_id=order_id).exists():
                    continue
                else:
                    break
             user = OrderList.objects.create(account_no=account_no,total_amount=total,order_id=order_id)
             user.save();
             Result = 'Order Order is  Placed will reached to within 10 day'
             messages.success(request,Result)
             Products = {'Carts': cart, 'User': user,'Log':log , 'total':total}
             return render(request, 'KIB-cart.html', Products)
            else:
             Result = 'YOUR ACCOUNT BALANCE IS LESS PLEASE DEPOSITE SOME CASH OR TAKE A LOAN'
             messages.error(request,Result)
             Products = {'Carts': cart, 'User': user,'Log':log , 'total':total}
             return render(request, 'KIB-cart.html', Products)
        Products = {'Carts': cart, 'User': user,'Log':log , 'total':total}
        return render(request, 'KIB-cart.html', Products)
    else:
        return redirect('/bazaar/')
