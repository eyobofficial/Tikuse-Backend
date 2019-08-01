from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='public_id', read_only=True)
    password = serializers.CharField(
        max_length=120,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'full_name',
            'phone_number',
            'role',
            'last_login',
            'date_joined'
        )

    def create(self, validated_data):
        raw_password = validated_data['password']
        user = User(
            username=validated_data['username'],
            full_name=validated_data['full_name'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role'],
        )
        user.set_password(raw_password)
        user.save()
        return user
