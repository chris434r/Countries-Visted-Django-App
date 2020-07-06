from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    lon = models.FloatField()
    lat = models.FloatField()
    fips = models.CharField(max_length=2, blank=True)
    iso2 = models.CharField(max_length=2, blank=True)

    objects = GeoManager()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the mode
    def __string__(self):
        return self.name
