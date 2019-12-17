from django.contrib import admin
from .models import DriveToWork, DistanceToWork, GasCardGiven


@admin.register(DriveToWork)
class DriveToWorkAdmin(admin.ModelAdmin):
    pass


@admin.register(DistanceToWork)
class DistanceToWorkAdmin(admin.ModelAdmin):
    pass

@admin.register(GasCardGiven)
class GasCardGivenAdmin(admin.ModelAdmin):
    pass