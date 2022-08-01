import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
import core.routing


# Note: do not change the import order 


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(URLRouter(core.routing.websocket_urlpatterns)),
})