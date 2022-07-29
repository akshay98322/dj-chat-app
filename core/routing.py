from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/wsc/<str:gname>/', consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/awsc/<str:gname>/', consumers.MyAsyncWebsocketConsumer.as_asgi()),
]