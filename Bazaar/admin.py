from django.contrib import admin
from .models import *

class MobileAdmin (admin.ModelAdmin):
    list_display = ('title' , 'price')

class ElectronicAdmin (admin.ModelAdmin):
    list_display = ('title' , 'price')

class FashionAdmin (admin.ModelAdmin):
    list_display = ('title' , 'price')

class HomeAdmin (admin.ModelAdmin):
    list_display = ('title' , 'price')

class BeautyAdmin (admin.ModelAdmin):
    list_display = ('title' , 'price')

class FurnitureAdmin (admin.ModelAdmin):
    list_display = ('title' , 'price')


class MedicineAdmin (admin.ModelAdmin):
    list_display = ('title' , 'price')


class ShoppingCartAdmin (admin.ModelAdmin):
    list_display = ('account_no' , 'title' , 'price')

class OrderListAdmin (admin.ModelAdmin):
    list_display = ('account_no' , 'total_amount' , 'order_id')

admin.site.register(Mobiles , MobileAdmin)
admin.site.register(Electronics , ElectronicAdmin)
admin.site.register(Fashion , FashionAdmin)
admin.site.register(Home , HomeAdmin)
admin.site.register(Beauty , BeautyAdmin)
admin.site.register(Furniture , FurnitureAdmin)
admin.site.register(Medicine , MedicineAdmin)
admin.site.register(ShoppingCart , ShoppingCartAdmin)
admin.site.register(OrderList , OrderListAdmin)

