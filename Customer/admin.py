from django.contrib import admin
from Customer.models import CredentialInfo , LoginInfo

class CredentialAdmin(admin.ModelAdmin):
    list_display = ('Account_No','total_deposite','open_time',)

class LoginAdmin(admin.ModelAdmin):
    list_display = ('Account_No','login_id','password',)


admin.site.register(CredentialInfo,CredentialAdmin)
admin.site.register(LoginInfo,LoginAdmin)
