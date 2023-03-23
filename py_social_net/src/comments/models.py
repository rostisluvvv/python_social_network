from django.db import models


class AbstractComment(models.Model):
    """
    Abstract base class for comments.

    Fields:
    - text (TextField): the message of the comment (up to 200 characters)
    - created_date (DateTimeField): the date and time the comment was created
    - update_date (DateTimeField): the date and time the comment was
    last updated
    - published (BooleanField): whether the comment is published or
    not (default is True)
    - deleted (BooleanField): whether the comment is deleted
    or not (default is False)

    Methods:
    - __str__(self): returns the text of the comment.

    Meta:
    - abstract = True: marks this class as an abstract base class,
    which means that it cannot be instantiated on its own,
    but can be subclassed by other classes.
    """
    text = models.TextField('message', max_length=200)
    created_date = models.DateTimeField('created date', auto_now_add=True)
    update_date = models.DateTimeField('update date', auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        abstract = True
