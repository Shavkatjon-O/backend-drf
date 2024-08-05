from rest_framework import generics

from apps.projects.api.ProjectCreate import serializers
from apps.projects import models


class ProjectCreateView(generics.CreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
