# from sms import send_sms
from twilio.rest import Client
from Home.models import AdminInfo
user = AdminInfo.objects.get(id=1)

def sms(otp, phone):
    TWILIO_ACCOUNT_SID = user.account_sid
    TWILIO_AUTH_TOKEN = user.account_token
    message = f'Your One Time Password is {otp}'
    client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
    client.messages.create(
        to=f'{phone}',
        from_=f'{user.phonenumber}',
        body=message
    )
