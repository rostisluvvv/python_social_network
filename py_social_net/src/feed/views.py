from rest_framework import generics, permissions, viewsets, response

from ..wall.serializers import ListPostSerializer
from .services import feed_services


class FeedView(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListPostSerializer

    def list(self, request, *args, **kwargs):
        queryset = feed_services.get_post_list(request.user)
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


