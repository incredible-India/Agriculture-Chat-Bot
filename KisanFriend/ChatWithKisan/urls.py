
from django.urls import path,include
from . import views

urlpatterns = [

 path('',views.index,name="index"),
 path('login',views.login,name="login"),
 path('weather', views.weather, name='weather'),
  path('scheme',views.scheme,name="scheme"),
  path('registration',views.register,name="registration"),
  path('logout',views.logout,name="logout"),
  path("chatHistory",views.chatHistory,name="chatHistory")

]


#d04b396f9cbf192128f6d1bad3b8296b api key weather 