from rest_framework import serializers

from .models import HostProfile, HostPhoto


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
            'address',
            'latitude',
            'longitude',
            'is_activated',
            'created_at',
            'updated_at',
            'photos'
        )
