
from django.urls import path,include
from . import views

urlpatterns = [

 path('',views.index,name="index"),
 path('login',views.login,name="login"),
  path('registration',views.register,name="registration"),
  path('logout',views.logout,name="logout"),
  path("chatHistory",views.chatHistory,name="chatHistory")

]
