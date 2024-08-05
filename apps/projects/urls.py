from django.urls import path

from apps.projects.api.ProjectCreate.views import ProjectCreateView


urlpatterns = [
    path("create/", ProjectCreateView.as_view(), name="project-create"),
]
