from .models import WorldBorder

from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse


def world(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiY2hyaXNyeWFuLXRlY2giLCJhIjoiY2thY2c3bDZyMDZsNDJ4cHJlZmhwZmFjaCJ9.3GuHRvRz-8fxi4r103z05w'
    return render(request, 'world/world.html',
                  {'mapbox_access_token': mapbox_access_token})


def Worldborders_GEOJSON(request):
    ready = serialize('geojson', WorldBorder.objects.all())
    return HttpResponse(ready, content_type='json')
