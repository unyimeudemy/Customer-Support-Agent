from django.urls import path
from .views import TelegramView
from . import views


urlpatterns = [
    path("", TelegramView.as_view()),
    path('task/1', views.add_new_task, name='add_new_task'),
    path('task/2', views.add_task_to_processing, name="add_task_to_processing"),
    path('task/3', views.add_task_to_done, name="add_task_to_done"),
    path('task/4', views.empty_redis_queue_and_list, name="empty_redis_queue_and_list")

]