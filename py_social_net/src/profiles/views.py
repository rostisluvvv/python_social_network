from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer


class UserNerPublicView(ModelViewSet):
    """
    A viewset that provides CRUD operations for the UserNet
    model with public access.

    Attributes:
    queryset: A queryset of all UserNet instances.
    serializer_class: The serializer class used to serialize UserNet
    instances.
    permission_classes: The permission classes used to authenticate and
    authorize requests.
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNetView(ModelViewSet):
    """
    A viewset that provides CRUD operations for the UserNet model
    with authenticated access.

    Attributes:
    serializer_class: The serializer class used to serialize UserNet
    instances.
    permission_classes: The permission classes used to authenticate and
    authorize requests.
    """
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
