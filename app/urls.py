from django.urls import path
from .views import UserProcessAPIView,TaskStatusAPIView

urlpatterns = [
    path('api/process-user/', UserProcessAPIView.as_view(), name='process-user'),
    path('api/task-status/<str:task_id>/', TaskStatusAPIView.as_view(), name='task-status'),

]
