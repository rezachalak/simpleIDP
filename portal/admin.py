from django.contrib import admin
from .models import Cloud, Cluster, Project

admin.site.register(Cluster)
admin.site.register(Project)
admin.site.register(Cloud)
