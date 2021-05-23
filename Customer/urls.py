from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.login),
    path('profile/',views.profile),
    path('profile/logout/',views.logout),

]