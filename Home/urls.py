from django.conf.urls import include
from django.urls import path
from . import views
from Transition import views as trnasition
from Bazaar import views as bazaar

urlpatterns = [
    path('',views.loader),
    path('home/',views.home),
    path('newaccount/',views.newaccount),
    path('login/',include('Customer.urls')),
    path('transition/',trnasition.transition),
    path('transition/<slug:user_id>/',trnasition.transition),
    path('bazaar/',bazaar.bazaar),
    path('bazaar/<slug:user_id>/',bazaar.bazaar),
    path('bazaar/cart/<slug:user_id>/',bazaar.cart),
]