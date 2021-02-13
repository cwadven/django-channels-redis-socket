  
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/test/<str:username>/', consumers.ChatConsumer.as_asgi()),
]