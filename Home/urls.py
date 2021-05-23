from django.urls import path
from . import views

urlpatterns = [
    path('',views.loader),
    path('home/',views.home),
]