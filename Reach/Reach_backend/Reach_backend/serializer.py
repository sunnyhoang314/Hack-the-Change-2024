from rest_framework import serializers
from .models import TaskRequest

class TaskRequestSerializer(serializers.ModelSerializer):
    class Meta:
        profile_image = serializers.ImageField(required=False, allow_null=True)
        task_image = serializers.ImageField(required=False, allow_null=True)
        model = TaskRequest
        fields = ['user_name', 'people_needed', 'task_description', 'profile_image', 'task_image', 'latitude', 'longitude', 'created_at']
