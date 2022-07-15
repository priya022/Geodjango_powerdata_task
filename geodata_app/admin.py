from django.contrib import admin

from django.contrib.gis import admin

from .models import US_states_info,Global_power_plant_info

admin.site.register(US_states_info, admin.GeoModelAdmin)
admin.site.register(Global_power_plant_info, admin.GeoModelAdmin)