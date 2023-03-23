from django.contrib.auth.models import AbstractUser
from django.db import models


class UserNet(AbstractUser):
    """
    A model representing a user, extending the AbstractUser
    class provided by Django.

    Methods:
    --------
    This class inherits all the methods from AbstractUser.
    """

    GENDER = (
        ('Man', 'Man'),
        ('Woman', 'Woman')
    )
    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/',
                               blank=True,
                               null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='Man')
    technology = models.ManyToManyField('Technology', related_name='users')


class Technology(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
