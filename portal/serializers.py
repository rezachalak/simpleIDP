from rest_framework import serializers
from .models import Cloud, Cluster, Project


class CloudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloud
        fields = "__all__"


class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
