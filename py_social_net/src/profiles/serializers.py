from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """Serializes UserNet model."""
    avatar = serializers.ImageField(write_only=True)

    class Meta:
        model = UserNet
        exclude = (
            'password',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """Serializes UserNet model for public."""

    class Meta:
        model = UserNet
        exclude = (
            'password',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',
            'email',
            'groups',
            'user_permissions',
            'phone'
        )


class UserByFollowerSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(write_only=True)

    class Meta:
        model = UserNet
        fields = ('id', 'username', 'avatar')
