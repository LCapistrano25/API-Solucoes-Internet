from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from groups.serializers import GroupModelSerializer
from django.contrib.auth.models import Group

class GroupListCreateAPIView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer

class GroupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer