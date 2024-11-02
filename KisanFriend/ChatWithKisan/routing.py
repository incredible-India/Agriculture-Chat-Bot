from django.urls import path
from .consumer import ConnectTOBot

websocket_urlpatterns = [
    path('ws/chat', ConnectTOBot.as_asgi()),
]
