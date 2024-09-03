from django.urls import path
from . import api_views

urlpatterns = [
    path("clouds/", api_views.CloudListCreate.as_view(), name="cloud-list-create"),
    path("clouds/<int:pk>/", api_views.CloudDetail.as_view(), name="cloud-detail"),
    path(
        "clusters/", api_views.ClusterListCreate.as_view(), name="cluster-list-create"
    ),
    path(
        "clusters/<int:pk>/", api_views.ClusterDetail.as_view(), name="cluster-detail"
    ),
    path(
        "projects/", api_views.ProjectListCreate.as_view(), name="project-list-create"
    ),
    path(
        "projects/<int:pk>/", api_views.ProjectDetail.as_view(), name="project-detail"
    ),
]
