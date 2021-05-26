from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('',views.loader),
    path('home/',views.home),
    path('newaccount/',views.newaccount),
    path('login/',include('Customer.urls')),
]