
from twilio.rest import Client
account_sid = "AC08ac8ff7e39df59fb1a45abea2bd3434"
auth_token  = "8a147e0d56b012a539e484bff327290d"
client = Client(account_sid, auth_token)

def sms(otp,phone):
   message = client.messages \
       .create(
       body=f"Your KIB ONE TIMA PASSWORD IS : {otp}",
       to=f"+91{phone}",
       from_="+18588341439",)
   print(message)



