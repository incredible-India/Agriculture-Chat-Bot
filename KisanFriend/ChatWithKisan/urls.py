
from django.urls import path,include
from . import views

urlpatterns = [

 path('',views.index),
 path('login',views.login,name="login"),
  path('registration',views.register,name="registration"),
  path('logout',views.logout,name="logout"),

]
