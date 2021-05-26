from django.contrib import admin
from .models import *

class Adminadmin(admin.ModelAdmin):
      list_display = ['debug']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','account_no','aadhar','pan')

class LoginAdmin(admin.ModelAdmin):
    list_display = ('Account_No','login_id','password',)


admin.site.register(AdminInfo,Adminadmin)
admin.site.register(CustomerInfo,CustomerAdmin)
admin.site.register(LoginInfo,LoginAdmin)


