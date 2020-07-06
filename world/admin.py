from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import WorldBorder


class WorldBorderAdmin(LeafletGeoAdmin):
    list_display = ('name', 'lon')


admin.site.register(WorldBorder, WorldBorderAdmin)
