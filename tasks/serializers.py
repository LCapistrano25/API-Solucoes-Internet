from rest_framework import serializers
from tasks.models import Task, Priority, Category
from django.contrib.auth.models import Group

class TaskModelSerializer(serializers.ModelSerializer):

    group_name = serializers.CharField(source='participants.name', required=False)
    priority_name = serializers.CharField(source='priority.name', required=False)
    category_name = serializers.CharField(source='category.name', required=False)
    participants_name = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'group_name', 'participants', 'participants_name', 
                  'category_name', 'category', 'priority_name', 'priority', 'date_start', 'date_end']

    def get_participants_name(self, obj):
        tasks = obj.participants
        names = []
        for participante in tasks.user_set.all():
            names.append(participante.username)

        return names
        
class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'status']

class PriorityModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Priority
        fields = ['id', 'name', 'status']
