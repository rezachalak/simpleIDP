from django.db import models
from django_softdelete.models import SoftDeleteModel

possible_provider = (('AWS','Amazon Web Service'), ('GCP','Google Cloud Provider'), ('Azure','Microsoft Azure'))
cluster_status_enum = ((1,'running'), (2,'stopped'), (3,'deprovisioning'), (4,'deprovisioning_failed'), (5,'provisioning'), (6,'provisioning_failed'))

class Cloud(SoftDeleteModel):
    name = models.CharField(max_length=100)
    provider = models.CharField(choices=possible_provider, max_length=10)
    access_key = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    endpoint = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' (' + self.provider + ')'

class Cluster(SoftDeleteModel):
    name = models.CharField(max_length=100)
    cloud = models.ForeignKey(Cloud, on_delete=models.PROTECT)
    status = models.IntegerField(choices=cluster_status_enum)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' on ' + self.cloud.name + ' with ' + self.size + ' of ' + self.type + ' type is ' + self.status

class Project(SoftDeleteModel):
    name = models.CharField(max_length=100)
    cluster = models.ForeignKey(Cluster, on_delete=models.PROTECT)

    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' in ' + self.cluster.name + ' on ' + self.cluster.cloud.name + ' with ' + self.cluster.size + ' of ' + self.cluster.type + ' type is ' + self.cluster.status
