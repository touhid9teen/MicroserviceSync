
from rest_framework import serializers
from . models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'phone_number', 'n_id', 'balance']


class CustomUserRegistationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number', 'n_id',
                  'name', 'balance', 'pin_code', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            n_id=validated_data['n_id'],
            name=validated_data['name'],
            balance=validated_data['balance'],
            pin_code=validated_data['pin_code'],
            password=validated_data['password']
        )
        return user
