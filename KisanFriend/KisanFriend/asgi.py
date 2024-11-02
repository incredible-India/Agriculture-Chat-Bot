"""
ASGI config for KisanFriend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from ChatWithKisan import routing as BotRouting
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KisanFriend.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket' : URLRouter(
        BotRouting.websocket_urlpatterns
    )
})
