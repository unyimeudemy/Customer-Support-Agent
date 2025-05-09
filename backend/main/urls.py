from django.urls import path
from .views import TelegramView


urlpatterns = [
    path("", TelegramView.as_view()),
]