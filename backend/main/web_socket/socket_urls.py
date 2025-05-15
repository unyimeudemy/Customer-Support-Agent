from django.urls import re_path
from .socket_consumers import (
    UnprocessedCustomerConsumer,
    CurrentlyProcessedCustomerConsumer,
)

websocket_urlpatterns = [
    re_path(r"ws/unprocessed_customers/$", UnprocessedCustomerConsumer.as_asgi()),
    re_path(r"ws/currently_processed_customer/$", CurrentlyProcessedCustomerConsumer.as_asgi()),

]