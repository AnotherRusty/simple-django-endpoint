from django.contrib import admin
from attendance.models import Checkin


class CheckinAdmin(admin.ModelAdmin):
    pass


admin.site.register(Checkin, CheckinAdmin)
