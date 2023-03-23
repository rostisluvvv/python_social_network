from rest_framework import permissions, generics

from ..base.classes import (CreateUpdateDestroy,
                            CreateRetrieveUpdateDestroy)
from ..base.permissions import IsAuthor
from .models import Post, Comment
from ..wall.serializers import (CreateCommentSerializer,
                                ListCommentSerializer,
                                PostSerializer,
                                ListPostSerializer)


class PostListView(generics.ListAPIView):
    """Список постов на стене пользователя"""
    serializer_class = ListPostSerializer

    def get_queryset(self):
        return Post.objects.filter(author_user_id=self.kwargs.get('pk'))


class PostView(CreateRetrieveUpdateDestroy):
    """CRUD поста """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)


class CommentsView(CreateUpdateDestroy):
    """CRUD коментариев"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes_by_action = {'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
