from django.contrib import admin
from .models import DriveToWork, DistanceToWork


@admin.register(DriveToWork)
class DriveToWorkAdmin(admin.ModelAdmin):
    pass


@admin.register(DistanceToWork)
class DistanceToWorkAdmin(admin.ModelAdmin):
    pass
