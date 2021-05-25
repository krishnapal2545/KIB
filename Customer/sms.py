from sms import send_sms

def sms(otp,phone):
   send_sms(
       f'Your Onle Time Password is : {otp}',
        '+18178542624',
        [f'{phone}'],
        fail_silently=True
    )