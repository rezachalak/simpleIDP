from rest_framework import generics
from .models import Cloud, Cluster, Project
from .serializers import CloudSerializer, ClusterSerializer, ProjectSerializer


class CloudListCreate(generics.ListCreateAPIView):
    queryset = Cloud.objects.all()
    serializer_class = CloudSerializer


class CloudDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cloud.objects.all()
    serializer_class = CloudSerializer


class ClusterListCreate(generics.ListCreateAPIView):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer


class ClusterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer


class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
