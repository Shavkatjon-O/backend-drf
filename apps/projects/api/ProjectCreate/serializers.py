from rest_framework import serializers
from apps.projects import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = (
            "id",
            "title",
            "start_date",
            "end_date",
            "priority",
            "description",
            "image",
        )
