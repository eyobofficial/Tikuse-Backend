from django.contrib.auth import get_user_model
from django.db import transaction

from allauth.account.adapter import get_adapter
from rest_framework import serializers

from .models import CustomUser, HostProfile, HostPhoto


User = get_user_model()


class BaseUserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='public_id', read_only=True)
    password = serializers.CharField(
        max_length=120,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        read_only_fields = ('role', )
        fields = (
            'id',
            'username',
            'phone_number',
            'password',
            'role',
            'last_login',
            'date_joined'
        )

    def validate_password(self, password):
        return get_adapter().clean_password(password)

    def create(self, validated_data):
        raw_password = validated_data['password']
        user = User(
            username=validated_data['username'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(raw_password)
        user.save()
        return user


class HostPhotoSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='public_id', read_only=True)

    class Meta:
        model = HostPhoto
        fields = ('id', 'photo', 'title', 'created_at')


class HostProfileSerializer(serializers.ModelSerializer):
    photos = HostPhotoSerializer(many=True)

    class Meta:
        model = HostProfile
        fields = (
            'full_name',
            'about',
            'profile_picture',
            'cover_picture',
            'email',
            'address',
            'latitude',
            'longitude',
            'religion',
            'is_activated',
            'created_at',
            'updated_at',
            'photos'
        )


class HostSerializer(BaseUserSerializer):
    full_name = serializers.CharField(max_length=120, write_only=True)
    profile = HostProfileSerializer(source='host', required=False)

    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + ('full_name', 'profile')

    @transaction.atomic
    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        user = super().create(validated_data)
        user.role = CustomUser.HOST
        user.save()

        # Add full_name to profile
        user.host.full_name = full_name
        user.host.save()

        return user
