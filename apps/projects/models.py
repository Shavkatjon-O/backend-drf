from django.db import models

from apps.common.models import BaseModel


class PriorityChoices(models.TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"


class Project(BaseModel):
    title = models.CharField(max_length=256)

    start_date = models.DateField()
    end_date = models.DateField()

    priority = models.CharField(max_length=16, choices=PriorityChoices.choices)
    description = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to="projects")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title
