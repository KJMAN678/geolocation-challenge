from django.contrib import admin

from stock.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("latitude", "longitude", "created_at")
