from rest_framework import generics, permissions, views, response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED

from ..profiles.models import UserNet
from .models import Follower
from .serializers import ListFollowerSerializer


class ListFollowerView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class FollowerView(views.APIView):
    """
    добавление в подписчики
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = UserNet.objects.filter(id=pk)
        if user.exists():
            Follower.objects.create(subscriber=request.user, user=user)
            return response.Response(status=HTTP_201_CREATED)
        return response.Response(status=HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.create(subscriber=request.user, user_id=pk)

        except Follower.DoesNotExist:
            return response.Response(status=HTTP_404_NOT_FOUND)
        sub.delete()
        return response.Response(status=204)






