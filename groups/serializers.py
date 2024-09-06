from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from django.contrib.auth.models import Group

class GroupModelSerializer(ModelSerializer):
    participants = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'name', 'participants']

    def get_participants(self, obj):

        participants = []

        for user in obj.user_set.all():
            participants.append(user.username)

        return participants
