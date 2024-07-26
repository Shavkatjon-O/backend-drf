import random

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

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


class OTP(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    code = models.CharField(max_length=6)
    active_till = models.DateTimeField(editable=False)

    @property
    def lifetime(self):
        time = self.active_till - timezone.now()
        return time.seconds

    @classmethod
    def get_new_code(cls):
        code = random.randint(100000, 999999)
        while OTP.objects.filter(code=code, active_till__gte=timezone.now()).exists():
            code = random.randint(100000, 999999)
        return str(code)

    @classmethod
    def otp_lifetime(cls, seconds):
        return timezone.now() + timezone.timedelta(seconds=seconds)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "OTP"
        verbose_name_plural = "OTPs"
