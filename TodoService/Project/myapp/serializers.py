from  rest_framework import serializers
from .models import TodoItem


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'

    def create(self, validated_data):
        return TodoItem.objects.create(**validated_data)