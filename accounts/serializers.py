from django.contrib.auth import get_user_model

from allauth.account.adapter import get_adapter
from rest_framework import serializers

from .models import HostProfile, HostPhoto


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
        read_only_fields = ('role', )
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

    def validate_password(self, password):
        return get_adapter().clean_password(password)

    def create(self, validated_data):
        raw_password = validated_data['password']
        user = User(
            username=validated_data['username'],
            full_name=validated_data['full_name'],
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
            'about',
            'email',
            'profile_picture',
            'cover_picture',
            'address',
            'latitude',
            'longitude',
            'is_activated',
            'created_at',
            'updated_at',
            'photos'
        )


class HostSerializer(UserSerializer):
    profile = HostProfileSerializer(source='host')

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('profile', )
