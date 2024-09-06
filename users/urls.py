from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy

urlpatterns = [
    path(
        'usuarios/', 
        UserListCreate.as_view(), 
        name='user-list-create'
    ),

    path(
        'usuarios/<int:pk>/', 
        UserRetrieveUpdateDestroy.as_view(), 
        name='user-retrieve-update-destroy'
    )
]