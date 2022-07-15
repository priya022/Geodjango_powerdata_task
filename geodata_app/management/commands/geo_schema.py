import os
import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		# convert the csv file to a DataFrame
		data = pd.read_csv(str(settings.BASE_DIR)+'\\geodata_app\\global_power_plant_database.csv', index_col=False)
		# extract the geometry from the DataFrame
		points = [Point(row['longitude'], row['latitude']) for key, row in data.iterrows()]
		#convert the DataFrame to a GeoDataFrame 
		geo_df = GeoDataFrame(data,geometry=points)
		# save the resulting shapefile
		geo_df.to_file('global_power_plant_database.shp', driver='ESRI Shapefile') 