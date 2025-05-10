from django.urls import path
from .views import TelegramView
from . import views


urlpatterns = [
    path("", TelegramView.as_view()),
    path('task/new/', views.add_new_task, name='add_new_task'),
    path('task/processing/', views.add_task_to_processing, name="add_task_to_processing"),
    path('task/done/', views.add_task_to_done, name="add_task_to_done")
]