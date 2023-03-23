from rest_framework import serializers

from ..base.serializers import RecursiveSerializer, FilterCommentListSerializer
from .models import Post, Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    """Добавление комментариев записей в посту """
    class Meta:
        model = Comment
        fields = ('post', 'text', 'parent')


class ListCommentSerializer(serializers.ModelSerializer):
    """Список комментариев записей к посту"""
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ('id',
                  'post',
                  'text',
                  'created_date',
                  'update_date',
                  'deleted',
                  'children')


class PostSerializer(serializers.ModelSerializer):
    """Вывод и редактирование поста """
    author_user = serializers.ReadOnlyField(source='author_user.username')
    comment = ListCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id',
                  'create_date',
                  'user_author',
                  'text',
                  'comment',
                  'view_count')


class ListPostSerializer(serializers.ModelSerializer):
    """Список записей в группе"""
    author_user = serializers.ReadOnlyField(source='author_user.username')

    class Meta:
        model = Post
        fields = ('id',
                  'create_date',
                  'user_author',
                  'text',
                  'comment',
                  'view_count',
                  'comments_count')


