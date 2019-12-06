from django.contrib import admin
from pingpong.models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass
