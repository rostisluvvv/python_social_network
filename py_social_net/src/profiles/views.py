from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions

from .models import UserNet
from .serializers import GetUserNetSerializer


class GetUserNetView(RetrieveAPIView):
    """
    Retrieves and serializes a single UserNet model
    instance for retrieval over a network.
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer


class UpdateUserNetView(UpdateAPIView):
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
