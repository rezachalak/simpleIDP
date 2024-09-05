from django.db import models
from django_softdelete.models import SoftDeleteModel
import os

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
output_type_enum = (
    ("JSON", "json"),
    # ("TEXT", "text"),
    # ("TABLE", "table")
)


class Cloud(SoftDeleteModel):
    name = models.CharField(max_length=100)
    provider = models.CharField(choices=possible_provider_enum, max_length=10)
    access_key = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    output = models.CharField(choices=output_type_enum, max_length=10, default="JSON")
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " (" + self.provider + ")"

    def load_credentials_as_env_vars(self):
        """
        Load the AWS credentials from this Cloud instance as environment variables.
        """
        os.environ["AWS_ACCESS_KEY_ID"] = self.access_key
        os.environ["AWS_SECRET_ACCESS_KEY"] = self.secret_key

        if self.region:
            os.environ["AWS_REGION"] = self.region

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()


class Cluster(SoftDeleteModel):
    name = models.CharField(max_length=100)
    cloud = models.ForeignKey(Cloud, on_delete=models.PROTECT)

    status = models.IntegerField(choices=cluster_status_enum)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    cluster_name = models.CharField(max_length=100)
    cluster_version = models.CharField(max_length=100, default="1.24")
    vpc_cidr = models.CharField(max_length=100, default="10.0.0.0/16")
    availability_zones = models.CharField(
        max_length=100, default='["eu-central-1a","eu-central-1b","eu-central-1c"]'
    )
    private_subnet_cidrs = models.CharField(
        max_length=100, default='["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]'
    )
    public_subnet_cidrs = models.CharField(
        max_length=100, default='["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]'
    )
    min_size = models.IntegerField(default=1)
    max_size = models.IntegerField(default=3)
    desired_size = models.IntegerField(default=2)
    instance_type = models.CharField(max_length=100, default="t2.medium")

    def __str__(self):
        return self.name + " on " + self.cloud.name + " (" + self.status + ")"

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()


class Project(SoftDeleteModel):
    name = models.CharField(max_length=100)
    cluster = models.ForeignKey(Cluster, on_delete=models.PROTECT)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " (" + self.cluster.name + " on " + self.cluster.cloud.name
