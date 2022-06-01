from django.contrib import admin

from BikeRentalApp.views import RentBike
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Vehicle)
admin.site.register(RentVehicle)

