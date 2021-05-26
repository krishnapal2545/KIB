from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.login),
    path('profile/<int:user_id>/',views.profile),
    path('profile/logout/<int:user_id>/',views.logout),
    path('profile/Edit/<int:user_id>/',views.edit),
    path('verify/<int:user_id>/',views.verify),

]