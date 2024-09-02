from django.urls import path
from tasks.views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView

urlpatterns = (
    path('tarefas/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tarefas/<int:pk>', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-retrieve-update-destroy')
)