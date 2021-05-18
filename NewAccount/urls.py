from django.urls import path
from . import views

urlpatterns = [
    path('',views.newaccount,name="newaccount"),
]