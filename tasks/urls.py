from django.urls import path
from tasks.views import (
    TaskListCreateAPIView, 
    TaskRetrieveUpdateDestroyAPIView, 
    PriorityListCreateAPIView, 
    PriorityRetrieveUpdateDestroyAPIView, 
    CategoryListCreateAPIView, 
    CategoryRetrieveUpdateDestroyAPIView
)

urlpatterns = (
    path(
        'tarefas/', 
        TaskListCreateAPIView.as_view(), 
        name='task-list-create'
    ),

    path(
        'tarefas/<int:pk>/', 
        TaskRetrieveUpdateDestroyAPIView.as_view(), 
        name='task-retrieve-update-destroy'
    ),

    path(
        'prioridades/', 
        PriorityListCreateAPIView.as_view(), 
        name='priority-list-create'
    ),

    path(
        'prioridades/<int:pk>/', 
        PriorityRetrieveUpdateDestroyAPIView.as_view(), 
        name='priority-retrieve-update-destroy'
    ),

    path(
        'categorias/', 
        CategoryListCreateAPIView.as_view(), 
        name='category-list-create'
    ),

    path(
        'categorias/<int:pk>/', 
        CategoryRetrieveUpdateDestroyAPIView.as_view(), 
        name='category-retrieve-update-destroy'
    )
    
)