from django.contrib import admin
from .models import Events,WeatherEvent,FlightList

# Register your models here.
admin.site.register(Events)
admin.site.register(WeatherEvent)
admin.site.register(FlightList)