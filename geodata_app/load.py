import os
from django.contrib.gis import geos

from django.contrib.gis.utils import LayerMapping
from .models import US_states_info,Global_power_plant_info

# Each key in the Powerplant dictionary corresponds to
# a field in the Powerplant model.
# Auto-generated `LayerMapping` dictionary for Powerplant model and US states info model
us_states_info_mapping = {
    'region': 'REGION',
    'division': 'DIVISION',
    'statefp': 'STATEFP',
    'statens': 'STATENS',
    'geoid': 'GEOID',
    'stusps': 'STUSPS',
    'name': 'NAME',
    'lsad': 'LSAD',
    'mtfcc': 'MTFCC',
    'funcstat': 'FUNCSTAT',
    'aland': 'ALAND',
    'awater': 'AWATER',
    'intptlat': 'INTPTLAT',
    'intptlon': 'INTPTLON',
    'geom': 'MULTIPOLYGON',
}

global_power_plant_mapping = {
    'country': 'country',
    'country_lo': 'country_lo',
    'name': 'name',
    'gppd_idnr': 'gppd_idnr',
    'capacity_m': 'capacity_m',
    'latitude': 'latitude',
    'longitude': 'longitude',
    'primary_fu': 'primary_fu',
    'other_fuel': 'other_fuel',
    'other_fu_1': 'other_fu_1',
    'other_fu_2': 'other_fu_2',
    'commission': 'commission',
    'owner': 'owner',
    'source': 'source',
    'url': 'url',
    'geolocatio': 'geolocatio',
    'wepp_id': 'wepp_id',
    'year_of_ca': 'year_of_ca',
    'generation': 'generation',
    'generati_1': 'generati_1',
    'generati_2': 'generati_2',
    'generati_3': 'generati_3',
    'generati_4': 'generati_4',
    'generati_5': 'generati_5',
    'generati_6': 'generati_6',
    'generati_7': 'generati_7',
    'estimated_field': 'estimated_',
    'estimate_1': 'estimate_1',
    'estimate_2': 'estimate_2',
    'estimate_3': 'estimate_3',
    'estimate_4': 'estimate_4',
    'estimate_5': 'estimate_5',
    'estimate_6': 'estimate_6',
    'estimate_7': 'estimate_7',
    'estimate_8': 'estimate_8',
    'estimate_9': 'estimate_9',
    'geom_point': 'MULTIPOINT',
}
state_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'tl_2021_us_state', 'tl_2021_us_state.shp'),
)
global_power_plant_csv = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'global_power_plant' ,'global_power_plant_database.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        US_states_info,state_shp , us_states_info_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)

    lm1 = LayerMapping(
        Global_power_plant_info, global_power_plant_csv, global_power_plant_mapping,transform=False, encoding='utf-8')
    lm1.save(strict=True, verbose=verbose)

