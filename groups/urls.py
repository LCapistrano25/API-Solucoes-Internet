from django.urls import path
from groups.views import GroupListCreateAPIView, GroupRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('grupos/', GroupListCreateAPIView.as_view(), name='group-list-create'),
    path('grupos/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view(), name='group-retrieve-update-destroy'),
]