from rest_framework import serializers
from tasks.models import Task, Priority, Category
from django.contrib.auth.models import Group

class TaskModelSerializer(serializers.ModelSerializer):

    participantes_name = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"

    def get_participantes_name(self, obj):
        grupo = Group.objects.get(id=obj.participants.id)
        
        print(grupo)

