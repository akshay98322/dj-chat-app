from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # socket consumers
    path('ws/sc/<str:gname>/', consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/<str:gname>/', consumers.MyAsyncConsumer.as_asgi()),
    # wessocket consumers
    path('ws/wsc/<str:gname>/', consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/awsc/<str:gname>/', consumers.MyAsyncWebsocketConsumer.as_asgi()),
    # json websocket consumers
    path('ws/jwc/<str:gname>/', consumers.MyJsonWebsocketConsumer.as_asgi()),
    path('ws/ajwc/<str:gname>/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),

]