from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.common.models import BaseModel
from apps.users.managers import UserManager


class User(AbstractUser, BaseModel):
    email = None
    first_name = None
    last_name = None

    full_name = models.CharField(max_length=256)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.username
