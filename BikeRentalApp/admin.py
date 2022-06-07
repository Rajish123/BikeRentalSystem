from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Vehicle)
admin.site.register(RentVehicle)
admin.site.register(Bill)
admin.site.register(Payment)


