from django.db import models


class AbstractComment(models.Model):
    text = models.TextField('message', max_length=200)
    created_date = models.DateTimeField('created date', auto_now_add=True)
    update_date = models.DateTimeField('update date', auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        abstract = True
