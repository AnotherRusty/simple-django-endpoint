from django.contrib import admin
from .models import Reflection


class ReflectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reflection, ReflectionAdmin)
