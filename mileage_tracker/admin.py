from django.contrib import admin
from .models import DriveToWork

@admin.register(DriveToWork)
class DriveToWorkAdmin(admin.ModelAdmin):
    pass
# Register your models here.
