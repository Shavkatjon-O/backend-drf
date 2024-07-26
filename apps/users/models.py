import random

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from apps.common.models import BaseModel
from apps.users.managers import UserManager


class PositionChoices(models.TextChoices):
    BUSINESS_OWNER = "business_owner", "Business Owner"
    PROJECT_MANAGER = "project_manager", "Project Manager"
    PRODUCT_MANAGER = "product_manager", "Product Manager"
    SOFTWARE_ENGINEER = "software_engineer", "Software Engineer"
    FRONTEND_ENGINEER = "frontend_engineer", "Frontend Engineer"
    BACKEND_ENGINEER = "backend_engineer", "Backend Engineer"
    QA_ENGINEER = "qa_engineer", "QA Engineer"
    DEVOPS_ENGINEER = "devops_engineer", "DevOps Engineer"
    UX_UI_DESIGNER = "ux_ui_designer", "UX/UI Designer"


class User(AbstractUser, BaseModel):
    username = None

    email = models.EmailField(unique=True)

    position = models.CharField(
        max_length=64, choices=PositionChoices.choices, null=True, blank=True
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email


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
