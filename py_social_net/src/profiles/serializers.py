from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """
    Serializes UserNet model instances for retrieval over a network.
    Excludes sensitive fields such as password, last login time,
    and admin privileges.
    """

    class Meta:
        model = UserNet
        exclude = ('password',
                   'last_login',
                   'is_active',
                   'is_staff',
                   'is_superuser')

