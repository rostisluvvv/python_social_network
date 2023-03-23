from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from ..wall.models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author_user',
        'moderation',
        'create_date',
        'published',
        'view_count',
        'id'
    )


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'post', 'created_date', 'published', 'id')
    mptt_level_indent = 15
