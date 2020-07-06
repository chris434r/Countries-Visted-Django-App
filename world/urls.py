from django.urls import path
from django.conf.urls import url
from . import views
from world.views import Worldborders_GEOJSON

urlpatterns = [

    path('', views.world),
    url('WorldBorders_GEOJSON_View', Worldborders_GEOJSON, name='borders_data'),

]
