from django.contrib import admin
from .models import AdminInfo

class Adminadmin(admin.ModelAdmin):
      list_display = ['debug']

admin.site.register(AdminInfo,Adminadmin)

# Register your models here.
