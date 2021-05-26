from django.contrib import admin
from .models import CredentialInfo 

class CredentialAdmin(admin.ModelAdmin):
    list_display = ('Account_No','total_deposite','open_time',)


admin.site.register(CredentialInfo,CredentialAdmin)
