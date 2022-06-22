from django.contrib.gis import admin
from .models import Note

admin.site.register(Note, admin.OSMGeoAdmin)