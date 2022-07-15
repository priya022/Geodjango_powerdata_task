from django.core.management.base import BaseCommand
from django.db.models import OuterRef, Subquery
from geodata_app.models import US_states_info,Global_power_plant_info
from django.db.models import DateTimeField, ExpressionWrapper, F

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		for power_plant in Global_power_plant_info.objects.all():
			power_plant.state = US_states_info.objects.filter(geom__contains = power_plant.geom_point).first()

