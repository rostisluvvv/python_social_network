from django.db import models
from django.conf import settings

from py_social_net.src.comments.models import AbstractComment


class Post(models.Model):
    text = models.TextField(max_length=750)
    create_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField(default=0)
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)

    def __str__(self):
        return f'Post by {self.author_user}'


class Comment(AbstractComment):
    pass