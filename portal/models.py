from django.db import models
from django_softdelete.models import SoftDeleteModel

possible_provider_enum = (
    ("AWS", "Amazon Web Service"),
    ("GCP", "Google Cloud Provider"),
    ("Azure", "Microsoft Azure"),
)
cluster_status_enum = (
    ("RUNNING", "running"),
    ("STOPPED", "stopped"),
    ("DEPROVISIONING", "deprovisioning"),
    ("DEPROVISION_FAILED", "deprovisioning_failed"),
    ("PROVISIONING", "provisioning"),
    ("PROVISION_FAILED", "provisioning_failed"),
)


class Cloud(SoftDeleteModel):
    name = models.CharField(max_length=100)
    provider = models.CharField(choices=possible_provider_enum, max_length=10)
    access_key = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    endpoint = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " (" + self.provider + ")"


class Cluster(SoftDeleteModel):
    name = models.CharField(max_length=100)
    cloud = models.ForeignKey(Cloud, on_delete=models.PROTECT)
    status = models.IntegerField(choices=cluster_status_enum)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " on " + self.cloud.name + " (" + self.status + ")"


class Project(SoftDeleteModel):
    name = models.CharField(max_length=100)
    cluster = models.ForeignKey(Cluster, on_delete=models.PROTECT)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " (" + self.cluster.name + " on " + self.cluster.cloud.name
