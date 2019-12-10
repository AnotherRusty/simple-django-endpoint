from django.contrib import admin
from attendance.models import Checkin


class CheckinAdmin(admin.ModelAdmin):
    list_display = ("student", "datetime", "verified")
    date_hierarchy = "datetime"


admin.site.register(Checkin, CheckinAdmin)
