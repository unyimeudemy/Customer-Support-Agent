from django.urls import re_path
from .socket_consumers import QueueConsumer

websocket_urlpatterns = [
    re_path(r"ws/queues/$", QueueConsumer.as_asgi()),
]