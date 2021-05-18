from django.contrib import admin
from .models import CustomerInfo

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','account_no','login_id','password')

admin.site.register(CustomerInfo,CustomerAdmin)
