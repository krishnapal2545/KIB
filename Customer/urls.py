from django.urls import path
from . import views
from Transition import views as trnasition

urlpatterns = [
    path('',views.login),
    path('profile/<slug:user_id>/',views.profile),
    path('profile/logout/<slug:user_id>/',views.logout),
    path('profile/Edit/<slug:user_id>/',views.edit),
    path('profile/verify/<slug:user_id>/',views.verify),
]